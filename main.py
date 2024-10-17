from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Глобальный массив для маршрута /list
global_list = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sum1n/{n}")
def sum1n(n: int):
    result = sum(range(1, n + 1))
    return {"result": result}

@app.get("/fibo")
def fibo(n: int):
    def fibonacci(num):
        a, b = 0, 1
        for _ in range(num):
            a, b = b, a + b
        return a
    
    result = fibonacci(n)
    return {"result": result}

@app.post("/reverse")
def reverse(string: str = Header(...)):
    result = string[::-1]
    return {"result": result}

# Модель для добавления элемента в глобальный массив
class Element(BaseModel):
    element: str


# Маршрут для добавления элемента в массив
@app.put("/list")
def add_to_list(item: Element):
    global global_list
    global_list.append(item.element)
    return {"result": global_list}

# Маршрут для получения глобального массива
@app.get("/list")
def get_list():
    return {"result": global_list}

# Модель для математического выражения
class Expression(BaseModel):
    expr: str

# Маршрут для калькулятора
@app.post("/calculator")
def calculator(expression: Expression):
    try:
        num1, operator, num2 = expression.expr.split(',')
        num1, num2 = float(num1), float(num2)
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise HTTPException(status_code=403, detail="zerodiv")
            result = num1 / num2
        else:
            raise HTTPException(status_code=400, detail="invalid")
        
        return {"result": result}
    
    except ValueError:
        raise HTTPException(status_code=400, detail="invalid")
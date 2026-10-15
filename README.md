

```
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --reload
```

Docs en `/docs`.



```
alembic revision --autogenerate -m "mensaje"
alembic upgrade head
alembic downgrade -1
```

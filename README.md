# Menu project  

## How to start:
1) Create new virtual environment and install project dependencies

```
pip install -r requirements.txt
```

2) Make migrations
```
python manage.py migrate
```

3) Load fixtures
```
py manage.py loaddatautf8 fixtures/user.json
py manage.py loaddatautf8 fixtures/compound.json
py manage.py loaddatautf8 fixtures/category.json
py manage.py loaddatautf8 fixtures/product.json

```

4) Run server
```
python manage.py runserver
```

Open admin panel [localhost:8000](http://localhost:8000/admin)

Default admin: admin

Default password: 123


(http://localhost:8000/api/categories/) - to list category

(http://localhost:8000/api/product/) - to display the full menu list

(http://localhost:8000/api/product/category/1) - to search by category (where 1 is the category id)


Open Swagger API documentation   (http://localhost:8000/schema/swagger/)

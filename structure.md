# Menu project

## apps

- categories
- compound
- product 

## Models

categories:  
    - name (varchar 70)
    - image (image field) 

compound 
    - name (varchar 70)

product
    - name (varchar 70)
    - category (fk category)
    - image (image field) 
    - price (int)
    - compound (m2m compound)
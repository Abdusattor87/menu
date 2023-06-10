# Menu project

## apps
- users
- categories
- compound
- product 

## Models

Users: 
    - User (abstactUser) 
    - id (uuid) 
    - username (string) 
    - email (email) 
    - first_name 
    - last_name
    
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
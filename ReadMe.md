
# Python Database

 Contributors: @Carter2565#5594, 
 This is the current database for PTSO-Exchange.
 This project can be used as a template for any python database.

## How to use:
### Launch:
*   Main.py tekes up to one arguement.
      -interface
        This enables a basic command line interface for testing requests.  For Example:
        
###       Command-Line
#
        [Python API] -- Server started http://localhost:8000

        Enter json: {Request}
        

###  Requests:
####  When sending a request it must a post method sending the nessary json:
```json
  { 
    "operation":"",
    "request": "",
    "login": "",
    "pwd": "",
    "username": ""
  }
```
#
1. For example this is a request for a __Users Data__
##### *  Not to be confused with __peofile data.__
  ```json
  {"operation":"get", "request": "user", "login": "2565tube@gmail.com", "pwd": "098f6bcd4621d373cade4e832627b4f6"},
  ``` 
2. A request for a __Users Profile Data__
  ```json
  {"operation":"get","request": "profile", "username": "Carter2565"},
  ```
3. A request for an __Asset__
  ```json
  {"operation":"get","request": "assets", "asset":"0"},
  ```
4. A request for the __Object File__
  ```json
  {"operation":"get","request": "object"}
  ```

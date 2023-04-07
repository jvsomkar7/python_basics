from flask import Flask, request, json, jsonify
from flask_restful import Resource, request, Api
#from models.employees.employees import connection as conn
# from models import config as conn
# from comman import config
import pandas as pd
# import json

class GetEmployee(Resource): #class define CAMEL IT MEANS 1ST LETTER CAPITAL AND MILLDE ONE CAPITAL
    def post(self):
        try:
            conn=config.connection()
            cur = conn.cursor()
            req_data = request.get_json()
            print(req_data)
            query = "select * from employess"
            df = pd.read_sql(query,conn)
            print(df)
            print(conn)                             #curd operations
            js = df.to_json(orient='records')
            print(js.__class__)

            #return json.loads(js)
            return {'res_status': True,
                                'status_code': 200,
                                        'employess': json.loads(js)}
        except Exception as e:
            print('error occurs')
        finally:
            cur.close()
            conn.close()





class updateEmployee(Resource):

    def post(self):
        try:
            conn=config.connection()
            req_data = request.get_json()
            print(req_data)
            emp_id =req_data['emp_id']
            emp_name = req_data['emp_name']
            emp_salary = req_data['emp_salary']
            query = f"UPDATE employess SET (emp_name,emp_salary)={emp_name,emp_salary} WHERE emp_id = {emp_id}"
            # update_script = f"UPDATE employees SET employee_data = {employee_data} where emp_id = {id}"

            print(conn)
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            return "update sucessfull"
        except Exception as e:
            print('error occurs')
        finally:
            cur.close()
            conn.close()


class insertEmployee(Resource):
    def post(self):
        try:
            conn=config.connection()
            req_data = request.get_json()
            print(req_data)
            emp_id = req_data['emp_id']
            emp_name = req_data['emp_name']
            emp_salary = req_data['emp_salary']

            value = f"INSERT INTO employess (emp_id ,emp_name,emp_salary) values('%d','%s','%d')"%(emp_id, emp_name,  emp_salary)
            cur = conn.cursor()
            cur.execute(value)
            print(conn)
            conn .commit()
            return {"status":200,"success":'insert sucessfull',"data":value}
        except Exception as e:
            # print('error occurs')
            return {"status":201,"failed":e}
        finally:
            cur.close()
            conn.close()


class deleteEmployee(Resource):
    def post(self):
        try:
            conn=config.connection()
            req_data = request.get_json()
            print(req_data)
            emp_id = req_data['emp_id']
            delete_script = f'DELETE FROM employess where emp_id = {emp_id}'
            cur = conn.cursor()
            cur.execute(delete_script)
            print(delete_script)
            print(conn)
            conn.commit()
            return 'delete sucessfull'
        except Exception as e:
            print('error occurs')
        finally:
            cur.close()
            conn.close()






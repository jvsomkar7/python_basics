from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from employees import GetEmployee,updateEmployee,insertEmployee,deleteEmployee

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(GetEmployee, '/get_emp')
api.add_resource(updateEmployee, '/update_emp')
api.add_resource(insertEmployee, '/insert_emp')
api.add_resource(deleteEmployee, '/delete_emp')
# app.run(host='DESKTOP-TOG9JLH', port=5000, debug=False, use_reloader=False)
app.run(host='DESKTOP-T3KOD4S', port=5432, debug=True, use_reloader=True)
if __name__=='__main__':
    app.run()

### omkar is awesome

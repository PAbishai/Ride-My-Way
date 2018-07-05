# Contains the models used by the documentation of the API

from flask_restplus import fields, Model


""" Register User
    ---
    Automatically documented model for register user
"""
user_model = Model('Test User',{
    'name':fields.String(
        required=True, 
        description='Full name of user',
        example="Test User"
    ),
    'email': fields.String(
        required=True,
        description='valid email of user',
        example='me@me.com'
    ),
    'password': fields.String(
        required=True,
        description='strong password for authentication',
        example='!!890@1'
    ),
    'dl_path':fields.String(
        description='path to uploaded drivers license',
        example='dls/me_dl.pdf'
    ),
    'car_reg':fields.String(
        description='the valid number plate of the car',
        example='KAA 111A'
    )

})
""" End of user_model
"""

""" Login User
    ---
    Automatically documented model for login user
"""
login_model = Model('Login Test User',{
    'email': fields.String(
        required=True,
        description='valid email of user',
        example='me@me.com'
    ),
    'password': fields.String(
        required=True,
        description='strong password for authentication',
        example='!!890@1'
    )
})
""" End of login_model
"""

""" Add Ride
    ---
    Automatically documented model for adding a Ride
"""
ride_model = Model('Test Ride',{
    'user_id':fields.Integer(
        required=True, 
        description='ID of driver creating ride',
        example=1
    ),
    'location': fields.String(
        required=True,
        description='where ride is coming from',
        example='Thika'
    ),
    'destination': fields.String(
        required=True,
        description='where the ride is headed',
        example='Nairobi CBD'
    ),
    'leaving':fields.String(
        description='time ride is starting',
        example='12:00 pm'
    )
})
""" End of rides_model definition
"""


""" Add Request
    ---
    Automatically documented model for adding a Ride
"""
request_model = Model('Test Request',{
    'passender_id': fields.Integer(
        required=True,
        description='id of passenger',
        example=2
    ),
    'pickup': fields.String(
        required=True,
        description='where passenger will be picked up',
        example='Ruiru'
    ),
    'dropoff':fields.String(
        description='where passenger will be allighting',
        example='Kasarani'
    ),
    'request_status':fields.String(
        description='status of join request',
        example='pending'
    )
})
""" End of request_model definition
"""   

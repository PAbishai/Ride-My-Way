from flask import Flask, jsonify, make_response, abort, request


app = Flask(__name__)

# Data structure to hold rides
#sample data

rides = []
ride_requests=[]


@app.route('/api/v1/rides', methods=['POST'])
def addRide():

    """ addRide() adds a ride to rides.
        ride_format = {
            "id":ride_id,
            "driver_id":user_id,
            "location_from":where ride starts,   
            "destination":destination,
            "leaving":time ride leaves,
            "full":checks whether ride is at capacity
        }
    """
    if not request.is_json:
        abort(400,"request not json")
    
    if not "driver_id" in request.get_json():
        abort(422,"driver_id missing")

    data = request.get_json()
    ride_id = len(rides)+1
    user_id = data["driver_id"]
    location_from = data["location"]
    destination = data["destination"]
    leaving = data["leaving"]
    full = False
    arrived = False

    ride = {
        "id":ride_id,
        "driver_id":user_id,
        "location":location_from,   
        "destination":destination,
        "leaving":leaving,
        "full":full,
        "arrived":arrived
    }

    rides.append(ride)

    return make_response(jsonify({"status":"created", "ride":ride}),201)
    
@app.route("/api/v1/rides", methods=["GET"])
def getRides():

    """ getrides() return a json string with a list of all rides when /api/v1/rides
        return a status message, rides list and 200 ok code
    """
    return make_response(jsonify({"status":"ok", "rides":rides}),200)
    

@app.route('/api/v1/rides/<int:ride_id>', methods=['GET'])
def getSingleRide(ride_id):
    
    """ getSingleRide() returns a single ride based on the ride id
        get ride["id"]=ride_id from the data source
    """
    #
    ride = [ride for ride in rides if ride["id"]==ride_id]
    
    #404 not found error if no ride with id is found
    if len(ride) == 0:
        abort(404)

    return make_response(jsonify({"status":"ok", "ride":ride}),200)



@app.route('/api/v1/rides/<int:ride_id>/requests', methods=['POST'])
def joinRequest(ride_id): 

    if not request.is_json:
        abort(400,"request not json")
    
    if not 'passenger_id' in request.get_json():
        abort(422,"passenger_id missing")
    
    data = request.get_json()
    passenger_id = data['passenger_id']
    pickup = data['pickup']

    join_request = {
        "id":len(ride_requests)+1,
        "ride_id":ride_id,
        "passenger_id":passenger_id,
        "pickup":pickup,
        "accepted":False
    }
    
    ride_requests.append(join_request)
    return make_response(jsonify({"status":"created","join_request":join_request, "all_requests":ride_requests}),201)
    

@app.errorhandler(400)
def badRequest(error):
    response = jsonify({"error":error.description})
    return response

@app.errorhandler(422)
def unprocessableEntity(error):
    response = jsonify({"error":error.description})
    return response


if __name__ == '__main__':
    app.run(debug=True)

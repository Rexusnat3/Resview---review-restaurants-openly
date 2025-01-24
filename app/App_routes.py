from flask import Flask, request, jsonify
import reviewer

app = Flask(__name__)
restaurantReviewer = reviewer.CuisinesRestaurantReviewer()

def route_initialization(app):
@app.route("/add_review", methods=["POST"])
def add_review():
    data = request.get_json()
    try:
        restaurantReviewer.add_review(
            data["restaurant_name"],
            data["reviewer_name"],
            data["rating"],
            data["comment"],
            data["cuisine_type"]
        )
        return jsonify ({"message":"Review successfully posted"}), 201
    except ValueError as e:
        return jsonify ({"error":str(e)}), 400


@app.route("/get_reviews", methods=["GET"])
def get_reviews(cuisine_type):
    reviews = restaurantReviewer.get_reviews_by_cuisine(cuisine_type)
    return jsonify (reviews), 200


if __name__ == "__main__":
    app.run(debug=True)
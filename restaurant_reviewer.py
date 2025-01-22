import json


class RestaurantReviewer:
    def __init__(self):
        self.reviews = []

    def add_review(self, restaurant_name, reviewer_name, rating, comment):
        """
        Adds a review to the system.

        Args:
            restaurant_name (str): The name of the restaurant.
            reviewer_name (str): The name of the reviewer.
            rating (int): Rating given by the reviewer (1-5).
            comment (str): A comment about the restaurant.

        Raises:
            ValueError: If rating is not between 1 and 5.
        """
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")

        review = {
            "restaurant_name": restaurant_name,
            "reviewer_name": reviewer_name,
            "rating": rating,
            "comment": comment
        }
        self.reviews.append(review)
        print(f"Review added for {restaurant_name} by {reviewer_name}.")

    def get_reviews_for_restaurant(self, restaurant_name):
        """
        Retrieves all reviews for a given restaurant.

        Args:
            restaurant_name (str): The name of the restaurant.

        Returns:
            list: A list of reviews for the restaurant.
        """
        return [review for review in self.reviews if review["restaurant_name"].lower() == restaurant_name.lower()]

    def get_average_rating(self, restaurant_name):
        """
        Calculates the average rating for a given restaurant.

        Args:
            restaurant_name (str): The name of the restaurant.

        Returns:
            float: The average rating or None if there are no reviews.
        """
        restaurant_reviews = self.get_reviews_for_restaurant(restaurant_name)
        if not restaurant_reviews:
            return None

        total_rating = sum(review["rating"] for review in restaurant_reviews)
        return total_rating / len(restaurant_reviews)

    def save_reviews_to_file(self, file_name):
        """
        Saves all reviews to a JSON file.

        Args:
            file_name (str): The name of the file to save reviews to.
        """
        with open(file_name, 'w') as file:
            json.dump(self.reviews, file, indent=4)
        print(f"Reviews saved to {file_name}.")

    def load_reviews_from_file(self, file_name):
        """
        Loads reviews from a JSON file.

        Args:
            file_name (str): The name of the file to load reviews from.
        """
        try:
            with open(file_name, 'r') as file:
                self.reviews = json.load(file)
            print(f"Reviews loaded from {file_name}.")
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty review list.")


# Subclass with additional functionality
class CategorizedRestaurantReviewer(RestaurantReviewer):
    def __init__(self):
        super().__init__()
        self.categorized_reviews = {}

    def add_review(self, restaurant_name, reviewer_name, rating, comment, cuisine_type):
        """
        Adds a review to the system with a cuisine type.

        Args:
            cuisine_type (str): The cuisine type of the restaurant.
        """
        super().add_review(restaurant_name, reviewer_name, rating, comment)

        # Add review to the categorized dictionary
        if cuisine_type not in self.categorized_reviews:
            self.categorized_reviews[cuisine_type] = []
        self.categorized_reviews[cuisine_type].append({
            "restaurant_name": restaurant_name,
            "reviewer_name": reviewer_name,
            "rating": rating,
            "comment": comment
        })

    def get_reviews_by_cuisine(self, cuisine_type):
        """
        Retrieves all reviews for a given cuisine type.

        Args:
            cuisine_type (str): The cuisine type.

        Returns:
            list: A list of reviews for the cuisine type.
        """
        return self.categorized_reviews.get(cuisine_type, [])


# Example usage
if __name__ == "__main__":
    categorized_reviewer = CategorizedRestaurantReviewer()

    categorized_reviewer.add_review("Pizza Palace", "Alice", 5, "Great pizza and friendly staff!", "Italian")
    categorized_reviewer.add_review("Sushi World", "Bob", 4, "Fresh and delicious sushi!", "Japanese")

    print("Reviews for Italian cuisine:", categorized_reviewer.get_reviews_by_cuisine("Italian"))
    print("Reviews for Japanese cuisine:", categorized_reviewer.get_reviews_by_cuisine("Japanese"))

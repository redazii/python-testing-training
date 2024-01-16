class RestaurantReviews:
    def __init__(self):
        self.reviews = {}

    def add_review(self, restaurant, review_text, rating):
        if rating < 1 or rating > 5:
            return "Invalid rating. It must be between 1 and 5."
        self.reviews[restaurant] = {'review_text': review_text, 'rating': rating}
        return f"Review added for {restaurant}."

    def get_review(self, restaurant):
        return self.reviews.get(restaurant, "Review not found.")

    def update_review(self, restaurant, new_review_text, new_rating):
        if restaurant not in self.reviews:
            return "Review not found."
        return self.add_review(restaurant, new_review_text, new_rating)
    
    def delete_review(self, restaurant):
        if restaurant not in self.reviews:
            return "Review not found."
        del self.reviews[restaurant]
        return f"Review deleted for {restaurant}."
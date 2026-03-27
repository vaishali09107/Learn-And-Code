import requests
import json

class TumblrApiClient:
    """Handles communication with Tumblr API v1"""

    BASE_URL = "https://{blog}.tumblr.com/api/read/json"

    def __init__(self):
        """Initialize default request parameters"""
        self.base_params = {
            "type": "photo"
        }

    def get_blog_data(self, blog_name, offset, limit):
        """Fetches photo posts from a Tumblr blog"""
        params = {
            **self.base_params,
            "start": offset,
            "num": limit
        }

        response = requests.get(
            self.BASE_URL.format(blog=blog_name),
            params=params
        )

        raw_text = response.text
        if raw_text.startswith("var tumblr_api_read = "):
            raw_text = raw_text[len("var tumblr_api_read = "):]

        return raw_text.rstrip().rstrip(";")

    def load_json(self, raw_text):
        """Converts API response text to JSON"""
        return json.loads(raw_text)

    def get_blog_metadata(self, data):
        """Extracts basic blog metadata"""
        return {
            "title": data["tumblelog"]["title"],
            "name": data["tumblelog"]["name"],
            "description": data["tumblelog"]["description"],
            "total_posts": data["posts-total"]
        }

    def collect_photo_links(self, posts, start_index):
        """Extracts photo URLs from blog posts"""
        photo_map = {}
        current_index = start_index

        for post in posts:
            urls = []

            if "photos" in post:
                for photo in post["photos"]:
                    urls.append(photo["photo-url-1280"])

            if urls:
                photo_map[current_index] = urls

            current_index += 1

        return photo_map

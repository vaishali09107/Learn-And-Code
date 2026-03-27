from blog_analyzer.fetch_api import TumblrApiClient
from blog_analyzer.input_handler import UserInputReader
from blog_analyzer.output_handler import ConsoleOutputRenderer

class TumblrApplication:
    """Coordinates the complete Tumblr blog analysis"""

    def start_application(self):
        input_handler = UserInputReader()
        api_client = TumblrApiClient()
        renderer = ConsoleOutputRenderer()

        blog_name = input_handler.get_blog_name()
        start, end = input_handler.get_post_range()

        start_index = start - 1
        count = end - start + 1

        raw_json = api_client.get_blog_data(blog_name, start_index, count)
        parsed_data = api_client.load_json(raw_json)

        blog_info = api_client.get_blog_metadata(parsed_data)
        renderer.display_blog_info(blog_info)

        photo_urls = api_client.collect_photo_links(parsed_data["posts"], start)
        renderer.display_photo_links(photo_urls)

if __name__ == "__main__":
    TumblrApplication().start_application()
 
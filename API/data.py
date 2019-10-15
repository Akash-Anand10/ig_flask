import requests
import json


def short_code_extractor(url):
    pass


def extract(short_code):
    base_url = "https://www.instagram.com/graphql/query/"
    query_hash = "33ba35852cb50da46f5b5e889df7d159"
    end_cursor = ""  # Initially we don't have an end cursor

    # short_code = "B1cZBetB3_T"

    comments = []

    s = requests.session()

    def fetch(base_url, short_code, query_hash, end_cursor=""):
        # start the session
        variables = f'{{"shortcode":"{short_code}","first":50,"after":"{end_cursor}"}}'
        params = {"query_hash": query_hash, "variables": variables}

        r = s.get(base_url, params=params)
        data = r.json()

        # fetch the actual data from the comments json
        edges = data["data"]["shortcode_media"]["edge_media_to_comment"]["edges"]
        page_info = data["data"]["shortcode_media"]["edge_media_to_comment"]["page_info"]
        has_next_page = page_info["has_next_page"]
        end_cursor = page_info["end_cursor"]

        for edge in edges:
            comments.append(edge)

        if has_next_page:
            fetch(base_url=base_url,short_code=short_code,query_hash=query_hash,end_cursor=end_cursor)

    try:
        fetch(base_url=base_url,short_code=short_code,query_hash=query_hash,end_cursor=end_cursor)
    except Exception as e:
        if type(e).__name__ == "TypeError":
            return "An error occured while fetching comments!! Please check if the Media URL is correct."
    else:
        json_comments = json.dumps(comments, ensure_ascii=False)
        return json_comments

def build_json_and_download(short_code, json_comments):
    with open(f"{short_code}.json", "w", encoding="utf-8") as text_file:
        text_file.write(json_comments)


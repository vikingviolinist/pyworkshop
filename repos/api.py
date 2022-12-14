import requests

from repos.exceptions import GitHubApiException
from repos.models import GitHubRepo

GITHUB_API_URL = "https://api.github.com/search/repositories"


def create_query(languages, min_stars):
    query = " ".join(f"language:{language.strip()}" for language in languages)
    query = query + f" stars:>{min_stars}"
    return query


def repos_with_most_stars(languages, min_stars=40000, sort="stars", order="desc"):
    query = create_query(languages, min_stars)
    params = {"q": query, "sort": sort, "order": order}
    response = requests.get(GITHUB_API_URL, params)

    if response.status_code != 200:
        raise GitHubApiException(response.status_code)

    response_json = response.json()
    items = response_json["items"]

    return [
        GitHubRepo(item["name"], item["language"], item["stargazers_count"])
        for item in items
    ]

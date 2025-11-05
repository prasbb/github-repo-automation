# from autogit import create_github_repo
# import requests

# def test_create_repo(monkeypatch):
#     def fake_post(url, headers, json):
#         class Resp: status_code=201; 
#         def json(self): return {"html_url":"https://github.com/test/repo"}
#         return Resp()
#     monkeypatch.setattr(requests, "post", fake_post)
#     create_github_repo("testrepo", "desc", False)

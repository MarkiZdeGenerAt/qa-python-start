import requests

def test_get_pikachu():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "pikachu"

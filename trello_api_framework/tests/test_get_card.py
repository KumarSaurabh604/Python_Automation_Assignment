from trello_api_framework.utils.api_client import TrelloApiClient
from trello_api_framework.utils.config_parser import ConfigParser


def test_get_card_with_valid_cardId_returns_200():
    client = TrelloApiClient()
    card_id = client.card_id
    response = client.get(endpoint=f"/cards/{card_id}")

    # Check the response status code
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['id'] == card_id

    ConfigParser().set_trello_config(key="id_List", value=response_data['idList'])


def test_get_card_with_Invalid_cardId_returns_400():
    client = TrelloApiClient()
    card_id = client.invalid_card_id
    response = client.get(endpoint=f"/cards/{card_id}")

    # Check the response status code
    assert response.status_code == 400, f'expected response code is {400}, but found {response.status_code}'

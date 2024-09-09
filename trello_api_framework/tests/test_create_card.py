import pytest
from trello_api_framework.utils.api_client import TrelloApiClient
from trello_api_framework.utils.trello_poco import CreateCard


def test_create_card_with_valid_idList_returns_200():
    client = TrelloApiClient()
    id_List = client.id_list
    queryParam = CreateCard(name="New Card", desc="Description of the new card", idList=id_List)
    response = client.post(endpoint="cards", param=queryParam.__dict__)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data['name'] == queryParam.name
    assert response_data['desc'] == queryParam.desc
    assert response_data['idList'] == queryParam.idList


def test_create_card_with_inValid_idList_returns_400():
    client = TrelloApiClient()
    invalid_id_list = client.invalid_id_list
    queryParam = CreateCard(name="New Card", desc="Description of the new card", idList=invalid_id_list)
    response = client.post(endpoint="cards", param=queryParam.__dict__)

    assert response.status_code == 400, f'expected response code is {400}, but found {response.status_code}'

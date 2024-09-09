from trello_api_framework.utils.api_client import TrelloApiClient
from trello_api_framework.utils.trello_poco import UpdateCard


def test_update_card_with_valid_cardId_returns_200():
    client = TrelloApiClient()
    card_id = client.card_id
    id_list = client.id_list
    updated_card = UpdateCard(name="Updated New Card", idList=id_list)
    response = client.put(endpoint=f"cards/{card_id}", param=updated_card.__dict__)

    assert response.status_code == 200
    response_data = response.json()
    print(response_data['id'])
    assert response_data['id'] == card_id


def test_update_card_with_inValid_cardId_returns_400():
    client = TrelloApiClient()
    card_id = client.invalid_card_id
    id_list = client.id_list
    updated_card = UpdateCard(name="Updated New Card", idList=id_list)
    response = client.put(endpoint=f"cards/{card_id}", param=updated_card.__dict__)

    assert response.status_code == 400, f'expected response code is {400}, but found {response.status_code}'


def test_update_card_with_inValid_idList_returns_400():
    client = TrelloApiClient()
    card_id = client.card_id
    id_List = client.invalid_id_list
    updated_card = UpdateCard(name="Updated New Card", idList=id_List)
    response = client.put(endpoint=f"cards/{card_id}", param=updated_card.__dict__)

    assert response.status_code == 400, f'expected response code is {400}, but found {response.status_code}'

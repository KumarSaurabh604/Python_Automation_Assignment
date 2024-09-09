from trello_api_framework.utils.api_client import TrelloApiClient
from trello_api_framework.utils.trello_poco import CreateCard


def test_delete_card_with_valid_cardId_returns_200():
    # card_id = "66d855915f4c21d60d65c95f"
    client = TrelloApiClient()
    id_List = client.id_list
    queryParam = CreateCard(name="New Card", desc="Description of the new card", idList=id_List)
    response = client.post(endpoint="cards", param=queryParam.__dict__)

    assert response.status_code == 200
    response_data = response.json()

    card_id = response_data['id']
    delete_response = client.delete(endpoint=f"cards/{card_id}")

    assert delete_response.status_code == 200


def test_delete_card_with_inValid_cardId_returns_400():
    card_id = "66d855915f4c21d60d65c95g"
    client = TrelloApiClient()
    response = client.delete(endpoint=f"cards/{card_id}")

    assert response.status_code == 400, f'expected response code is {400}, but found {response.status_code}'


def test_delete_card_with_empty_cardId_returns_404():
    card_id = ""
    client = TrelloApiClient()
    response = client.delete(endpoint=f"cards/{card_id}")

    assert response.status_code == 404, f'expected response code is {404}, but found {response.status_code}'
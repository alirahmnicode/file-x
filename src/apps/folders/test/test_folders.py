from django.contrib.auth import get_user_model
from rest_framework import status
import pytest

User = get_user_model()


@pytest.fixture
def create_folder(api_client, authenticate):
    def do_create_folder(folder):
        return api_client.post("/api/folders/", folder)
    return do_create_folder

    
@pytest.mark.django_db
class TestCreateFolder:
    def test_if_user_is_anonymus_returns_401(self, api_client):
        response = api_client.post("/api/folders/")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_data_is_valid_return_201(self, authenticate, create_folder):
        response = create_folder({"title": "a"})

        assert response.status_code == status.HTTP_201_CREATED
        assert list(response.data.keys()) == ["id", "title"]

    def test_if_data_is_invalid_return_400(self, authenticate, create_folder):
        response = create_folder({"title": ""})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] is not None


@pytest.mark.django_db
class TestRetrieveFolder:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        response = api_client.get("/api/folders/")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_retrieve_all_folders_returns_200(self, api_client, authenticate, create_folder):
        folder_1 = create_folder({"title": "a"})
        folder_2 = create_folder({"title": "a"})
        response = api_client.get("/api/folders/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0
        assert response.data[0]["title"] == "a"

    def test_retrieve_single_folder_returns_200(self, api_client, authenticate, create_folder):
        folder = create_folder({"title": "a"})
        folder_id = folder.data["id"]
        response = api_client.get(f"/api/folders/{folder_id}/")

        assert response.status_code == status.HTTP_200_OK  
        assert response.data["title"] == "a"

    def test_if_folder_id_is_incorrect_returns_404(self, api_client, authenticate):
        response = api_client.get(f"/api/folders/4/")
        
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] is not None
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_create_address_success():
    response = client.post(
        "/address/create",
        json={
            "street": "Dr. Lyuben Popov",
            "city": "Varna",
            "country": "Bulgaria",
            "latitude": 43.219613,
            "longitude": 27.950008,
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        "street": "Dr. Lyuben Popov",
        "city": "Varna",
        "country": "Bulgaria",
        "latitude": 43.219613,
        "longitude": 27.950008,
    }


def test_create_address_failure():
    response = client.post(
        "/address/create",
        json={
            "country": "Bulgaria",
            "latitude": 43.219613,
            "longitude": 27.950008,
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "street"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "city"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ]
    }


def test_read_address_success():
    response = client.get("/address/read/1")
    assert response.status_code == 200
    assert response.json() == {
        "street": "Dr. Lyuben Popov",
        "city": "Varna",
        "country": "Bulgaria",
        "latitude": 43.219613,
        "longitude": 27.950008,
    }


def test_read_address_failure():
    response = client.get("/address/read/100")
    assert response.status_code == 404
    assert response.json() == {"detail": "Address not found"}


def test_update_address_success():
    response = client.put(
        "/address/update/1",
        json={
            "street": "Dr. Lyuben Popov",
            "city": "Sofia",
            "country": "Bulgaria",
            "latitude": 43.219613,
            "longitude": 27.950008,
        },
    )
    assert response.status_code == 200
    assert response.json() == "Address with id 1 updated successfully"


def test_update_address_failure():
    response = client.put(
        "/address/update/100",
        json={
            "street": "Dr. Lyuben Popov",
            "city": "Sofia",
            "country": "Bulgaria",
            "latitude": 43.219613,
            "longitude": 27.950008,
        },
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Address not found"}


def test_delete_address_success():
    response = client.delete("/address/delete/1")
    assert response.status_code == 200
    assert response.json() == "Address with id 1 deleted successfully"


def test_delete_address_failure():
    response = client.delete("/address/delete/100")
    assert response.status_code == 404
    assert response.json() == {"detail": "Address not found"}


def test_get_nearby_addresses_success():
    client.post(
        "/address/create",
        json={
            "street": "Dr. Test",
            "city": "Sofia",
            "country": "Bulgaria",
            "latitude": 43.219613,
            "longitude": 27.950008,
        },
    )
    client.post(
        "/address/create",
        json={
            "street": "Dr. Lyuben Popov",
            "city": "Varna",
            "country": "Bulgaria",
            "latitude": 43.219613,
            "longitude": 27.950008,
        },
    )
    response = client.get("address/nearby/1?distance=0.1")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 2,
            "city": "Varna",
            "latitude": 43.219613,
            "country": "Bulgaria",
            "street": "Dr. Lyuben Popov",
            "longitude": 27.950008,
        }
    ]


def test_get_nearby_addresses_failure():
    response = client.get("address/nearby/100?distance=0.1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Address not found"}

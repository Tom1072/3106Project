import pytest
from server.app.services.ChessService import ChessService

@pytest.fixture(scope="function")
def chess_service() -> ChessService:
    return ChessService()
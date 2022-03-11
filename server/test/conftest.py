import pytest
from app.ChessService import ChessService

@pytest.fixture(scope="function")
def chess_service() -> ChessService:
    return ChessService()
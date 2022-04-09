
from wagon_common.path.scope import Scope


class TestScope():

    def test_scope(self):

        # Arrange

        # Act
        scope = Scope.from_sources(["."])

        # Assert
        assert scope.repo.tld is not None

        # Cleanup

from Source_data.details import details
import pytest
from Utils.Base_custom_logger import Base_custome_logger


class Test_callable(details, Base_custome_logger):

    @pytest.mark.cli
    def test_callable(self):
        log = self.logging()
        log.info("Memory file execution is started")

        self.memory_display()
        USAGE = details.memory_display(self)

        if 90 >= USAGE[1]:
            assert True
            log.info("Memory size is" + str(USAGE[1]))
            log.info("Memory is in the range")

        else:
            log.info("High memory usage")
            log.info("Memory size is" + str(USAGE[1]))
            assert False

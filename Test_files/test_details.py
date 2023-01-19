import paramiko

from Source_data.details import details
import pytest
from Utils.Base_custom_logger import Base_custome_logger


class Test_callable(details, Base_custome_logger):

    # @pytest.mark.cli
    # def test_vm_connection(self):
    #     log = self.logging()
    #     log.info("ssh connection of vm")
    #     details.vm_connection(self)
    #     log.info("ssh connection establish")

    @pytest.mark.cli
    def test_callable(self):
        log = self.logging()
        log.info("Memory file execution is started")

        self.memory_display()
        log.info("ssh connection of vm")
        details.vm_connection(self)
        log.info("ssh connection establish")
        USAGE = details.memory_display(self)

        if 90 >= USAGE[1]:

            assert True
            log.info("Memory size in % is - " + str(USAGE[1]))
            log.info("Memory is in the range")
            log.info("Successful execution")
        else:
            log.info("High memory usage")
            log.info("Memory size in % is - " + str(USAGE[1]))
            log.info("unsuccessful execution")
            assert False

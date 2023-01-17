from details import details
import pytest


class Test_callable(details):

    @pytest.mark.cli
    def test_callable(self):
        # self.logger.info("Memory file execution is started")
        self.memory_display()
        CPU_USAGE = details.memory_display(self)
        print("+++++++++++++++++++++++")
        print(CPU_USAGE)

        if 20 >= CPU_USAGE:
            assert True
            print("++++++++++++++++++++++++++")
            print("Memory is in the range")

        else:
            print("High memory usage")
            assert False


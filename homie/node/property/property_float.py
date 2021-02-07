import logging
# non std modules
from .property_base import Property_Base

logger = logging.getLogger(__name__)


class Property_Float(Property_Base):
    """ generic float property """

    def __init__(
        self,
        node,
        id,
        name,
        settable=True,
        retained=True,
        qos=1,
        unit=None,
        data_type="float",
        data_format=None,
        value=None,
        set_value=None,
        tags=[],
        meta={},
    ):
        super().__init__(
            node,
            id,
            name,
            settable,
            retained,
            qos,
            unit,
            "float",
            data_format,
            value,
            set_value,
            tags,
            meta,
        )
        # valid data_formats:
        # <low>:        only lower value is defined
        # <None>:<high> only high is defined
        # <low>:<high>  low and high are defined
        #
        if data_format: # like low_value:high_value
            _range = data_format.split(":")
            if len(_range) == 2: # both, low and high are available, but low could be None
                if _range[0]:
                    self.low_value = float(_range[0])
                if _range[1]:
                    self.high_value = float(_range[1])
            elif len(_range) == 1: # only low is defined, like <low>:
                self._low_value = float(_range[0])
        else:
            self.low_value = None
            self.high_value = None

    def validate_value(self, value):
        """ check if value is on defined range """
        valid = True
        if self.low_value and value < self.low_value:
            valid = False
        if self.high_value and value > self.high_value:
            valid = False
        return valid

    def get_value_from_payload(self, payload):
        """ convert payload to float, or return None """
        try:
            return float(payload)
        except:
            return None

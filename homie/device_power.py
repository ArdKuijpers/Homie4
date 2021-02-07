#!/usr/bin/env python
import logging
# non std modules
from homie.device_status import Device_Status
from homie.node.property.property_power import Property_Power

logger = logging.getLogger(__name__)


class Device_Power(Device_Status):
    """ Power measuring Device in watts """

    def __init__(
        self,
        device_id=None,
        name=None,
        homie_settings=None,
        mqtt_settings=None,
    ):
        super().__init__(device_id, name, homie_settings, mqtt_settings)

    def register_status_properties(self, node):
        self.power = Property_Power(node)
        node.add_property(self.power)

    def update_power(self, power):
        logger.info("Updated Power {}".format(power))
        self.power.value = power


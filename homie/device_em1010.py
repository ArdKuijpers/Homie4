#!/usr/bin/env python
import logging
# non std modules
from homie.device_status import Device_Status
from homie.node.property.property_power import Property_Power
from homie.node.property.property_energy import Property_Energy

logger = logging.getLogger(__name__)


class Device_EM1010(Device_Status):
    """ Device to measure power and energy consumption """

    def __init__(
        self,
        device_id=None,
        name=None,
        homie_settings=None,
        mqtt_settings=None,
    ):
        super().__init__(device_id, name, homie_settings, mqtt_settings)

    def register_status_properties(self, node):
        self.power = Property_Power(node) # actual power in W
        node.add_property(self.power)
        self.energy = Property_Energy(node) # actual work in kW/h
        node.add_property(self.energy)
        self.total_energy = Property_Energy(node) # actual work in kW/h
        node.add_property(self.total_energy)

    def update_temperature(self, power):
        logger.info("Updated Power {} W".format(power))
        self.power.value = power

    def update_energy(self, energy):
        logger.info("Updated Energy {} kW/h".format(energy))
        self.energy.value = energy

    def update_total_energy(self, total_energy):
        logger.info("Updated Total Energy {} kW/h".format(total_energy))
        self.total_energy.value = total_energy


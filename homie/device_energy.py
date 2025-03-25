import logging

from homie.device_status import Device_Status
from homie.node.node_base import Node_Base
from homie.node.property.property_energy import Property_Energy

logger = logging.getLogger(__name__)


class Device_Energy(Device_Status):
    """ Device to measure energy consumption """

    def __init__(
        self,
        device_id=None,
        name=None,
        homie_settings=None,
        mqtt_settings=None,
    ):
        super().__init__(device_id, name, homie_settings, mqtt_settings)

    def register_status_properties(self, node: Node_Base):
        self.energy = Property_Energy(node)
        node.add_property(self.energy)

    def update_energy(self, energy):
        logger.info("Updated Energy {}".format(energy))
        self.energy.value = energy



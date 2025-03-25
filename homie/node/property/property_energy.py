from .property_float import Property_Float


class Property_Energy(Property_Float):
    """ measuring energy in kWh """

    def __init__(
        self,
        node,
        id="energy",
        name="Energy",
        settable=False,
        retained=True,
        qos=1,
        unit="kWh",
        data_type=float,
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
            data_type,
            data_format,
            value,
            set_value,
            tags,
            meta,
        )


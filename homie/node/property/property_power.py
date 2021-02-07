from .property_float import Property_Float


class Property_Power(Property_Float):
    """ measuring power in Watts """

    def __init__(
        self,
        node,
        id="power",
        name="Power",
        settable=False,
        retained=True,
        qos=1,
        unit="W",
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


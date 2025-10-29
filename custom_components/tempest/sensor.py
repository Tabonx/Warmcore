from homeassistant.helpers.entity import Entity

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([ExampleSensor()])

class ExampleSensor(Entity):
    def __init__(self):
        self._state = "Hello World"

    @property
    def name(self):
        return "Example Sensor"

    @property
    def state(self):
        return self._state


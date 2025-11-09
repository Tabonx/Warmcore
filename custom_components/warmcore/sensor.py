from homeassistant.helpers.entity import Entity
from homeassistant.helpers.event import async_track_state_change_event
from . import DOMAIN


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the warmcore sensor using the domain configuration."""
    input_entity = hass.data[DOMAIN]["input_entity"]
    add_entities([WarmcoreSensor(hass, input_entity)])


class WarmcoreSensor(Entity):
    """Sensor that mirrors tht value of another sensor + 1."""

    def __init__(self, hass, input_entity):
        self.hass = hass
        self._input_entity = input_entity
        self._state = None

        async_track_state_change_event(hass, [input_entity], self._state_changed)

    @property
    def name(self):
        return f"warmcore {self._input_entity.split('.')[-1]}"

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return "unit"

    def _state_changed(self, event):
        new_state = event.data.get("new_state")
        if new_state is None:
            return
        try:
            self._state = float(new_state.state) + 1
        except ValueError:
            self._state = new_state.state
        self.schedule_update_ha_state()

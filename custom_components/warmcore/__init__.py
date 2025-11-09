"""warmcore integration"""

"""warmcore domain-style integration"""

from homeassistant.helpers.discovery import load_platform

DOMAIN = "warmcore"


def setup(hass, config):
    """Set up the warmcore integration."""
    conf = config.get(DOMAIN, {})
    input_entity = conf.get("input_entity")
    if not input_entity:
        return False

    hass.data[DOMAIN] = {"input_entity": input_entity}

    # Load the sensor platform internally
    load_platform(hass, "sensor", DOMAIN, {}, config)
    return True

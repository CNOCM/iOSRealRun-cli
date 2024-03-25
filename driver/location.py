from pymobiledevice3.cli.developer import LocationSimulation
from pymobiledevice3.services.simulate_location import DtSimulateLocation
from pymobiledevice3.lockdown import LockdownClient


def set_location(service_provider: LockdownClient, lat: float, lng: float):
    DtSimulateLocation(service_provider).set(lat, lng)


def clear_location(service_provider: LockdownClient):
    DtSimulateLocation(service_provider).clear()


def set_location_17(dvt, lat: float, lng: float):
    LocationSimulation(dvt).set(lat, lng)


def clear_location_17(dvt):
    LocationSimulation(dvt).clear()

"""
_summary_
"""
import json
import threading
import time
from typing import Union

import serial


class SerialObject():
    """ Serial Object Class """

    def __init__(
        self,
        *args,
        port: Union[str, None] = None,
        baudrate: int = 9600,
        bytesize: int = 8,
        parity: str = "N",
        stopbits: float = 1,
        timeout: Union[float, None] = None,
        **kwargs,
    ):
        super(SerialObject, self).__init__(*args, **kwargs)
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout

        self.serial: serial.Serial

    def __enter__(self):
        self.serial = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            bytesize=self.bytesize,
            parity=self.parity,
            stopbits=self.stopbits,
            timeout=self.timeout,
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.serial.close()

    def read(self):
        """ Read Serial and Return """
        return self.serial.read()

    def read_yield(self):
        """ Read Serial and Yield """
        while True:
            time.sleep(0.05)
            yield self.serial.read()

    @staticmethod
    def read_yield_simulate():
        """ Simulation of Read Serial and Yield """

        analog_value = 256
        current_time = 123456
        temperature = 25.5
        humidity = 45.6
        water_temperature = 24.8
        air_quality = 35

        while True:
            time.sleep(3)
            light_level = analog_value

            if light_level < 105:
                light_status = "Işık yeterli, fotosentez yapılıyor"
            else:
                light_status = "Işık yetersiz, dinlenme sürecinde"

            # output = f"Analog Value: {analog_value} | Time: {current_time} | Temperature: {temperature}C | Humidity: {humidity}% | DS18B20 Temp: {water_temperature}ºC / {water_temperature * 1.8 + 32}ºF | Air Quality: {air_quality}PPM | Light Level: {light_level} - {light_status}"

            # print(output)
            _output = json.dumps(
                {
                    "analog_value": analog_value,
                    "current_time": current_time,
                    "temperature": temperature,
                    "humidity": humidity,
                    "water_temperature": water_temperature,
                    "air_quality": air_quality,
                    "light_level": light_level,
                    "light_status": light_status,
                }
            )
            yield _output

    def task(self):
        """ Thread Task """
        thread = threading.Thread(
            target=self.read_yield_simulate, name='read_yield_simulate')

        time.sleep(0.05)
        print("Thread is starting...")
        thread.start()
        print("Thread is running...")
        time.sleep(0.03)

        thread.join()


if __name__ == "__main__":
    # with SerialObject(port="COM3") as serial_object:
    #     for data in serial_object.read_yield_simulate():
    #         print(data)
    SerialObject().task()
    while True:
        time.sleep(1)
        print(".")

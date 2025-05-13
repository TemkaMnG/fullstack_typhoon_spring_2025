"""
Дасгал 1: Үндсэн Удамшил.
------------------------
Доорх Тээврийн хэрэгсэл (Vehicle) классын бүтцийг гүйцээнэ үү.
- Vehicle-ээс удамшсан Car болон Motorcycle классуудыг хэрэгжүүлнэ үү
- Тохирох аттрибут болон методуудыг нэмнэ үү
- Дэд классуудад display_info методыг дахин тодорхойлно уу
"""
class Vehicle:
    """Тээврийн хэрэгслийн үндсэн класс."""

    def __init__(self, make: str, model: str, year: int):
        """Vehicle классын байгуулагч.

        Args:
            make: Үйлдвэрлэгч
            model: Загвар
            year: Үйлдвэрлэсэн он
        """
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self) -> str:
        """Тээврийн хэрэгслийг асаах."""
        self.is_running = True
        return f"{self.make} {self.model} асаалаа"

    def stop(self) -> str:
        """Тээврийн хэрэгслийг унтраах."""
        self.is_running = False
        return f"{self.make} {self.model} унтраалаа"

    def display_info(self) -> str:
        """Тээврийн хэрэгслийн мэдээллийг харуулах."""
        return f"{self.year} оны {self.make} {self.model}"


# TODO: Vehicle-ээс удамшсан Car классыг хэрэгжүүлнэ үү
# Car нь нэмэлт аттрибуттай байх: num_doors, fuel_type
# display_info-г дахин тодорхойлж эдгээр аттрибутуудыг оруулна уу
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year, num_doors, fuel_type):



# TODO: Vehicle-ээс удамшсан Motorcycle классыг хэрэгжүүлнэ үү
# Motorcycle нь нэмэлт аттрибуттай байх: engine_cc, has_sidecar
# display_info-г дахин тодорхойлж эдгээр аттрибутуудыг оруулна уу
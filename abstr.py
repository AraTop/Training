from abc import ABC, abstractmethod

class Transport(ABC):

   @abstractmethod
   def start_engine(self):
      pass
   
   @abstractmethod
   def stop_engine(self):
      pass

   @abstractmethod
   def move(self):
      pass

   @abstractmethod
   def stop(self):
      pass


class Boat(Transport):
   def start_engine(self):
      return "Катер громко затарахтел"
   
   def stop_engine(self):
      return "Двигатель катера чихнул напоследок и заглох"
  
   def move(self):
      return "Катер быстро набирает скорость"

   def stop(self):
      return "Катер остановился"

class Car(Transport):
   def start_engine(self):
      return "Машина заурчала двигателем"
   
   def stop_engine(self):
      return "Машина стоит с заглушенным двигателем"
  
   def move(self):
      return "Машина едет к цели назначения"

   def stop(self):
      return "Машина остановилась"
   
class Electroscooter(Transport):
   def start_engine(self):
      return "Мигнул светодиодом"
   
   def stop_engine(self):
      return "Мигнул светодиодом дважды"
  
   def move(self):
      return "Прохожие в ужасе разбегаются от очередного камикадзе"

   def stop(self):
      return "Торможение об стену прошло успешно"
   
class Person():
   def use_transport(self ,transport: Transport):
      transport.move()
      transport.start_engine()
      transport.stop()
      transport.stop_engine()
      return ""
from threading import Event

class BranchEvent( ):
  
  def __init__( self ):
    self.__event = Event()
    self.__links = []

  def add_link( self, event ):
    if self.__links.count( event ) == 0:
      self.__links.append(event)

  def remove_link( self, event ):
    self.__links.remove(event)

  def set( self ):
    self.__event.set()
    for event in self.__links:
      event.set()

  def clear( self ):
    self.__event.clear()
    for event in self.__links:
      event.clear()    

  def wait( self ):
    self.__event.wait()

  def is_set( self ):
    return self.__event.is_set()

  def isSet( self ):
    return self.__event.isSet()

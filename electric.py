from threading import Event


class LinkedEvent( object ):
  
  def __init__( self ):
    self._event = Event()
    self._links = []

  def add_link( self, event ):
    if self._links.count( event ) == 0:
      self._links.append(event)

  def remove_link( self, event ):
    self._links.remove(event)

  def get_links( self ):
    return self._links

  def set( self ):
    raise NotImplementedError("Abstract method cannot be called")

  def clear( self ):
    raise NotImplementedError("Abstract method cannot be called")

  def wait( self ):
    raise NotImplementedError("Abstract method cannot be called")

  def is_set( self ):
    raise NotImplementedError("Abstract method cannot be called")

  def isSet( self ):
    raise NotImplementedError("Abstract method cannot be called")



class BranchEvent( LinkedEvent ):
  
  def set( self ):
    self._event.set()
    for event in self._links:
      event.set()

  def clear( self ):
    self._event.clear()
    for event in self._links:
      event.clear()    

  def wait( self ):
    self._event.wait()

  def is_set( self ):
    return self._event.is_set()

  def isSet( self ):
    return self._event.isSet()


class HubEvent( LinkedEvent ):

  def add_link( self, event ):
    if isinstance( event, BranchEvent ):
      super( HubEvent, self ).add_link( event )
      event.add_link( self )
    else:
      raise TypeError("BranchEvent required")

  def wait( self ):
    self._event.wait()

  def is_set( self ):
    return self._event.is_set()

  def isSet( self ):
    return self._event.isSet()



class ANDHubEvent( HubEvent ):
  
  def set( self ):
    all_set = True
    for event in self.get_links():
      all_set = all_set and event.isSet()
    if all_set:
      self._event.set()

  def clear( self ):
    any_clear = False
    for event in self.get_links():
      any_clear = any_clear or not event.is_set()
      if any_clear:
         break
    if any_clear:
      self._event.clear()



class ORHubEvent( HubEvent ):
  
  def set( self ):
    any_set = False
    for event in self.get_links():
      any_set = any_set or event.isSet()
      if any_set:
        break
    if any_set:
      self._event.set()

  def clear( self ):
    all_clear = True
    for event in self.get_links():
      all_clear = all_clear and not event.is_set()
    if all_clear:
      self._event.clear()

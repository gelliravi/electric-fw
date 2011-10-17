import unittest
from linkedevents import LinkedEvent

class LinkedEventsTest( unittest.TestCase ):

  def setUp( self ):
    self.event1 = LinkedEvent()
    self.event2 = LinkedEvent()
    self.event3 = LinkedEvent()

  def test_is_set_and_clear( self ):
    self.assertFalse( self.event1.is_set() )
    self.event1.set()
    self.assertTrue( self.event1.is_set() )
    self.event1.clear()
    self.assertFalse( self.event1.is_set() )

  def test_add( self ):
    self.event1.add_link( self.event2 )

  def test_remove( self ):
    with self.assertRaises( ValueError ):
      self.event1.remove_link( self.event2 )
    self.event1.add_link( self.event2 )
    self.event1.remove_link( self.event2 )

  def test_links_no_lateral( self ):
    self.event1.add_link( self.event2 )
    self.event1.add_link( self.event3 )
    self.assertFalse( self.event1.is_set() )
    self.assertFalse( self.event2.is_set() )

  def test_1_to_2( self ):
    self.event1.add_link( self.event2 )
    self.event1.add_link( self.event3 )    
    self.event1.set()
    self.assertTrue( self.event2.is_set() )
    self.assertTrue( self.event3.is_set() )
    self.event1.clear()
    self.assertFalse( self.event2.is_set() )
    self.assertFalse( self.event3.is_set() )

  def test_transitive( self ):
    self.event1.add_link( self.event2 )
    self.event2.add_link( self.event3 )    
    self.event1.set()
    self.assertTrue( self.event2.is_set() )
    self.assertTrue( self.event3.is_set() )
    self.event1.clear()
    self.assertFalse( self.event2.is_set() )
    self.assertFalse( self.event3.is_set() )

  def test_no_duplicates( self ):
    self.event1.add_link( self.event2 )
    self.event1.add_link( self.event2 )
    self.event1.remove_link( self.event2 )
    with self.assertRaises( ValueError ):
      self.event1.remove_link( self.event2 )

if __name__ == '__main__':
  unittest.main()

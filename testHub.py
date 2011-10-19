import unittest
from electric import BranchEvent, ANDHubEvent, ORHubEvent


class ANDHubEventTest( unittest.TestCase ):

  def setUp( self ):
    self.event1 = BranchEvent()
    self.event2 = BranchEvent()
    self.event3 = ANDHubEvent()

  def _test_is_set_and_clear( self ):
    self.assertFalse( self.event1.is_set() )
    self.event1.set()
    self.assertTrue( self.event1.is_set() )
    self.event1.clear()
    self.assertFalse( self.event1.is_set() )

  def test_add( self ):
    self.event3.add_link( self.event1 )

  def test_remove( self ):
    with self.assertRaises( ValueError ):
      self.event3.remove_link( self.event1 )
    self.event3.add_link( self.event1 )
    self.event3.remove_link( self.event1 )

  def test_links_no_lateral( self ):
    self.event3.add_link( self.event1 )
    self.event3.add_link( self.event2 )
    self.assertFalse( self.event1.is_set() )
    self.assertFalse( self.event2.is_set() )
    self.assertFalse( self.event3.is_set() )    
 
  def test_2_to_1( self ):
    self.event3.add_link( self.event1 )
    self.event3.add_link( self.event2 )    
    self.event1.set()
    self.assertFalse( self.event3.is_set() )
    self.event2.set()
    self.assertTrue( self.event3.is_set() )
    self.event2.clear()
    self.assertFalse( self.event3.is_set() )



class ORHubEventTest( unittest.TestCase ):

  def setUp( self ):
    self.event1 = BranchEvent()
    self.event2 = BranchEvent()
    self.event3 = ORHubEvent()

  def _test_is_set_and_clear( self ):
    self.assertFalse( self.event1.is_set() )
    self.event1.set()
    self.assertTrue( self.event1.is_set() )
    self.event1.clear()
    self.assertFalse( self.event1.is_set() )

  def test_add( self ):
    self.event3.add_link( self.event1 )

  def test_remove( self ):
    with self.assertRaises( ValueError ):
      self.event3.remove_link( self.event1 )
    self.event3.add_link( self.event1 )
    self.event3.remove_link( self.event1 )

  def test_links_no_lateral( self ):
    self.event3.add_link( self.event1 )
    self.event3.add_link( self.event2 )
    self.assertFalse( self.event1.is_set() )
    self.assertFalse( self.event2.is_set() )
    self.assertFalse( self.event3.is_set() )    
 
  def test_2_to_1( self ):
    self.event3.add_link( self.event1 )
    self.event3.add_link( self.event2 )    
    self.event1.set()
    self.assertTrue( self.event3.is_set() )
    self.event2.set()
    self.assertTrue( self.event3.is_set() )
    self.event2.clear()
    self.assertTrue( self.event3.is_set() )
    self.event1.clear()
    self.assertFalse( self.event3.is_set() )

if __name__ == '__main__':
  unittest.main()

import pytest
from television import Television

def test_init():
    t = Television()
    assert str(t) == 'Power=False, Channel=0, Volume=0'
    
def test_power():
    t = Television()
    assert str(t) == 'Power=False, Channel=0, Volume=0'
    
    t.power()
    assert str(t) == 'Power=True, Channel=0, Volume=0'
    
    t.power()
    assert str(t) == 'Power=False, Channel=0, Volume=0'
    
def test_mute():
    t = Television()
    
    t.mute()
    assert str(t) == 'Power=False, Channel=0, Volume=0'


    t.power()

    t.volume_up()
    assert str(t) == 'Power=True, Channel=0, Volume=1'


    t.mute()
    assert str(t) == 'Power=True, Channel=0, Volume=0'


    t.mute()
    assert str(t) == 'Power=True, Channel=0, Volume=1'

    t.power()  
    t.mute()
    assert str(t) == 'Power=False, Channel=0, Volume=1'
    
def test_channel_up():
    t = Television()
    assert str(t) == 'Power=False, Channel=0, Volume=0'
    
    t.channel_up()
    assert str(t) == 'Power=False, Channel=0, Volume=0'
    
    t.power()
    t.channel_up()
    assert str(t) == 'Power=True, Channel=2, Volume=0'
    
    t.channel_up()
    t.channel_up()
    assert str(t) == 'Power=True, Channel=0, Volume=0'
    
def test_channel_down():
    t = Television()
    assert str(t) == 'Power=False, Channel=0, Volume=0'
    
    t.power()
    t.channel_down()
    t.channel_down()
    t.channel_down()
    assert str(t) == 'Power=True, Channel=3, Volume=0'
    
def test_volume_up():
    t = Television()
    assert str(t) == 'Power=False, Channel=0, Volume=0'
    
    t.volume_up()
    assert str(t) == 'Power=False, Channel=0, Volume=0' 
    
    t.power()
    t.volume_up()
    assert str(t) == 'Power=True, Channel=0, Volume=1'
    
    t.mute()
    t.volume_up()  
    assert str(t) == 'Power=True, Channel=0, Volume=2'
    
    t.volume_up()  
    assert str(t) == 'Power=True, Channel=0, Volume=2'

def test_volume_down():
    t = Television()
    assert str(t) == 'Power=False, Channel=0, Volume=0'
    
    t.power()
    t.volume_up()
    t.volume_up()
    t.volume_down()
    assert str(t) == 'Power=True, Channel=0, Volume=1'
    
    t.mute()
    t.volume_down()  
    assert str(t) == 'Power=True, Channel=0, Volume=0'
    
    t.volume_down()  
    assert str(t) == 'Power=True, Channel=0, Volume=0'
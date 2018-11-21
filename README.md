# ros_blinkstick_square_driver

### blinkstick ROS node
**Subscribes to**
* set_all_led _(Set color as RGB (ColorRGBA msgs))_
* set_single_led _(Set color of led A as RGB (ColorRGBA msgs))_

**Description**:  
In the _set_all_led_ all LEDs are set accordingly to the **R**, **G**, ang **B** values (0-255). **A** is not used.  
In the _set_single_led_ the LED specified by **A** (0-7) is set accordingly to the **R**, **G**, ang **B** values (0-255)

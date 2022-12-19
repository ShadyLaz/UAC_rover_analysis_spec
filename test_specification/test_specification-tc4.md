# Test specification

## tc4

### 

The temperature should affect the efficiency of the solar panels 

- **Test name:** Weather module efficiency
- **Test filename:** weatherModule
- **Test type:** functional test
- **Test level:** L2
- **Test created by:** Shady


## Preconditions

| **Action**                                                   | **Expected outcome**                                |
|:-------------------------------------------------------------|:----------------------------------------------------|
| - Solar panels unfold <br/> - Change temperature/environment | - Solar panels unfolded<br/> - Change in efficiency |  


## Test

| **Action**                       | **Expected outcome**     |
|:---------------------------------|:-------------------------|
| check efficiency of solar panels | output of the efficiency |   


## Postconditions

| **Action**                                    | **Expected outcome** |
|:----------------------------------------------|:---------------------|
| change back to normal environment/temperature | max efficiency       |

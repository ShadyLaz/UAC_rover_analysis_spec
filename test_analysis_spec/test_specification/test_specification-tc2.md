# Test specification
## Weather Module
## tc2

### Description

 Module should not make a new measurement if previous was done less than 30 seconds ago

- **Test name:** weather module 30 seconds measurements
- **Test filename:** weatherModule
- **Test type:** unit test
- **Test level:** L0
- **Test created by:** Shady


## Preconditions

| **Action**           | **Expected outcome** |
|:---------------------|:---------------------|
| require measurements | measurements output  |


## Test

| **Action**                                                                                                         | **Expected outcome**                                |
|:-------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------|
| - call for new measurements in under 30s of last measurement <br/> - call for new measurements with 30s in between | - output last measurements <br/> - new measurements |


## Postconditions

| **Action** | **Expected outcome**   |
|:-----------|:-----------------------|
| N/A        | N/A                    |

# Test specification

## tc1

### Description

Max efficiency loss due to temperature is 0.6 

- **Test name:** Max efficiency loss
- **Test filename:** weatherModule
- **Test type:** QA
- **Test level:** L1
- **Test created by:** Shady


## Preconditions

| **Action**         | **Expected outcome** |
|:-------------------|:---------------------|
| change temperature | efficiency loss      |


## Test

| **Action**            | **Expected outcome**       |
|:----------------------|:---------------------------|
| check efficiency loss | max efficiency loss is 0.6 |


## Postconditions

| **Action**                           | **Expected outcome** |
|:-------------------------------------|:---------------------|
| change temperature back to required  | max efficiency       |

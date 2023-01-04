# Requirement analysis

## Required enablers

1. Drop battery to lower 2.3 Volts. REQ-id 1
2. Charge battery to 4.2 Volts. Req-id 2
3. Restart. REQ-id 3
4. Change environment. REQ-id 4


### weather module

| **REQ-id** | **Test type** | **Test level** | **Notes**         |
|:-----------|:--------------|:---------------|:------------------|
| 1          | QA            | L1             | functional test   | 
| 2          | QA            | L1             | Functional test   |
| 3          | QA            | L0             | Functional test   |
| 4          | QA            | L0             | Functional test   |

### Module name

| **REQ-id** | **Test type** | **Test level** | **Notes** |
|:-----------|:--------------|:---------------|:----------|
|            |               |                |           |

## Test cases identified

| **REQ-id** | **Test case id** | **Test level** | **Notes**                                   |
|:-----------|:-----------------|:---------------|:--------------------------------------------|
| 1          | ts1              | L1             | Drop battery charge to lower than 2.3 volts |
| 2          | ts2              | L1             | Charge battery to 4.2 volts                 |
| 3          | ts3              | L0             | Restart                                     | 
| 4          | ts4              | L0             | Change environment                          |
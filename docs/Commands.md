## Project management commands:

-   [x] OPEN **[NEW]** PROJECT **{Name}**
-   [x] SAVE PROJECT **{Name}**
-   [x] RUN PROJECT

## Program navigation commands:

-   [x] READ LINE|LINES **{number}** TO **{number}** | [THE] END
-   [ ] STOP READING
-   [ ] [GO TO THE] **[beginning of | end of]** LINE **{number}**
-   [x] CHANGE LINE **{number}** TO **{command}**

## Memory commands:

-   [x] CREATE VARIABLE **{name}**
-   [x] CREATE ARRAY **{name}** [INCLUDES **{values}**]
-   [x] SORT **{name}** NUMERICALLY|ALPHABETICALLY
-   [x] SET **{name}** [EQUAL] TO **{value}**
-   [x] SEPARATE **{name}** BY **{value}**
    -   Takes a string and creates an array of strings, split by **{value}**.
-   [x] COMMENT ... END COMMENT
-   [x] JOIN **{name}** TO **{name}** [AS **{name}**]
    -   If the third name exists, assign the result to that variable, otherwise assign it to the first.

## Math commands:

### Basic Math Commands

-   [ ] ADD **{number}** AND **{number}**
    -   [AND **{number}**] statement can be repeated
-   [ ] SUBTRACT **{number}** BY **{number}**
-   [ ] DIVIDE **{number}** BY **{number}**
-   [ ] MULTIPLY **{number}** BY **{number}**
-   [ ] SQUARE ROOT OF **{number}**
-   [ ] **{number}** POWER OF **{number}**
-   [ ] ADD **{variable}** AND **{variable}**
    -   For string concetenation and number variables
-   [ ] SUBTRACT **{variable}** BY **{variable}**

## Output commands:

-   [x] SAY [VARIABLE] **{number}**
    -   Use speech synthesis to dictate the value of the variable
-   [x] PRINT [VARIABLE] **{number}**
    -   Display the contents of the variable on the console

## Input commands:

### ** TO DO **

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

-   [x] ADD **{number}** AND **{number}**
-   [x] [AND **{number}**] statement can be repeated
-   [x] SUBTRACT **{number}** BY **{number}**
-   [x] DIVIDE **{number}** BY **{number}**
-   [x] MULTIPLY **{number}** BY **{number}**
-   [x] SQUARE ROOT OF **{number}**
-   [x] **{number}** POWER OF **{number}**
-   [x] ADD **{variable}** AND **{variable}**
    -   For string concetenation and number variables
-   [x] SUBTRACT **{variable}** BY **{variable}**
-   [ ] Absolute value - ABSOLUTE VALUE OF **{variable}**
-   [ ] Minimum/Maximum value (in a list) - MINIMUM VALUE OF **{variable}** / MAXIMUM VALUE OF **{variable}** 
-   [ ] Random Integer - SET **{variable}** TO RANDOM VALUE
-   [ ] Exponent - SET **{variable}** TO THE POWER OF **{variable}**
-   [x]Mean - MEAN OF **{variable}**
-   [x]Median - MEDIAN OF **{variable}**
-   [x]Mode - MODE OF **{variable}** 
-   [ ]Standard Deviation - STANDARD DEVIATION OF **{variable}**
-   [ ]Graph Plot - PLOT {variable}** AND **{variable}**
-   [ ]Correlation - CORRELATION OF **{variable}**

## Graphics Commands

-	[ ]DRAW **{shape}** HEIGHT **{value}** WIDTH **{value}** COLOR **{color}**
	-	possibly add more commands for thickness and color diversity
-	[ ]IMAGE ADD **{variable name}**
	-	a file selector/url paster will pop up
-	[ ]IMAGE DELETE **{variable name}**
	-	hovering over an image will show its variable name if you forget it
 
## Output commands:

-   [x] SAY [VARIABLE] **{number}**
    -   Use speech synthesis to dictate the value of the variable
-   [x] PRINT [VARIABLE] **{number}**
    -   Display the contents of the variable on the console

## Input commands:

### ** TO DO **

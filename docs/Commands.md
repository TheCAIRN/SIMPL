## Project management commands:

-   [x] OPEN **[NEW]** PROJECT **{Name}**
-   [x] SAVE PROJECT **{Name}**
-   [x] RUN PROJECT

## Program navigation commands:

-   [x] READ LINE | LINES **{number}** TO **{number}** | [THE] END
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
-   [ ] ABSOLUTE VALUE OF **{variable}**
-   [ ] MINIMUM VALUE OF **{variable}**
-   [ ] MAXIMUM VALUE OF **{variable}** 
-   [ ] SET **{variable}** TO RANDOM VALUE
    -   For assigning random numbers     
-   [ ] SET **{variable}** TO THE POWER OF **{variable}**
    -   For exponents   
-   [x] MEAN OF **{variable}**
-   [x] MEDIAN OF **{variable}** 
-   [x] MODE OF **{variable}** 
-   [ ] STANDARD DEVIATION OF **{variable}**
-   [ ] PLOT {variable}** AND **{variable}** (for graphing points on a plot)
-   [ ] CORRELATION OF **{variable}** 

## Graphics Commands

-	[x] DRAW **{size}** **{color}** **{shape}** AT | IN **{location}**
	-	EX phrase: draw a large blue circle in middle
	-	possibly add more commands for thickness and color diversity
-	[x] WRITE **{text}** **{line)** OPTIONAL **{font}** OPTIONAL **{indent}** 
	-	EX phrase: write "the trees blew south" on line 4 with arial font single indent
-	[ ] IMAGE ADD **{variable name}**
	-	a file selector/url paster will pop up
-	[ ] IMAGE DELETE **{variable name}**
	-	hovering over an image will show its variable name if you forget it
 
## Output commands:

-   [x] SAY [VARIABLE] **{number}**
    -   Use speech synthesis to dictate the value of the variable
-   [x] PRINT [VARIABLE] **{number}**
    -   Display the contents of the variable on the console

## Input commands:

## Database Connectivity Commands:
- [ ] CONNECT TO DATABASE **{Name}**
- [ ] LOGIN AS **{userid}** WITH PASSWORD **{password | passphrase}**
  -   When setting up the database, create allowed users and set up recorded passphrases to compare and verify
- [ ] VIEW TABLE ** {Table Name} **
- [ ] SELECT ALL FROM ** {Table Name} **
- [ ] STOP CONNECTION TO DATABASE **{Name}**

### ** TO DO **

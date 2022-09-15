GREP
(Pattern search in file of for file)
--------------------------------------------------------

get grep

sudo apt-get install grep
-------------------------------------------------------

grep 'word' filename

grep 'word' file1 file2 file3

grep 'string1 string2' filename

cat otherfile | grep 'something'

command | grep 'something'

command option1 | grep 'data'

grep --color 'data' filename

-------------------------------------------------------

Search /etc/passwd for UserX

grep UserX /etc/passwd
----------------------------

Ignore case -i

grep -i "userx" /etc/passwd

or

cat /etc/passwd | grep -i "userx"

------------------------------------

Recursive search -r -R

grep -r "searchterms" /etc/

or

grep -R "searchterms" /etc/

------------------------------------

grep -E 

--extended -regex

interprets the pattern as a basic regular expression
(i think it interprets it as part of a string)

----------------------------------------------------------------

$ find / -xdev -type f -print0 2>/dev/null | xargs -0 grep -E '^[a-z0-9]{32}$' 2>/dev/null

find files and convert to std output  | take output and use as input/ convert to std input/ fiind the pattern
'line begins^ [from a-z and from 0-9]{with 32 charactors}$end of line' / send errors to the voidq
q


 Anchoring
       The  caret  ^  and  the  dollar  sign  $  are  meta-characters that respectively match the empty string at the
       beginning and end of a line.



 Character Classes and Bracket Expressions
       A  bracket  expression  is  a list of characters enclosed by [ and ].  It matches any single character in that
       list; if the first character of the list is the caret ^ then it matches any character not in  the  list.   For
       example, the regular expression [0123456789] matches any single digit.

       Within  a bracket expression, a range expression consists of two characters separated by a hyphen.  It matches
       any single character that sorts between the two characters, inclusive, using the locale's  collating  sequence
       and  character  set.   For example, in the default C locale, [a-d] is equivalent to [abcd].  Many locales sort
       characters in dictionary order, and in these locales [a-d] is typically not equivalent to [abcd]; it might  be
       equivalent  to  [aBbCcDd],  for example.  To obtain the traditional interpretation of bracket expressions, you
       can use the C locale by setting the LC_ALL environment variable to the value C.


 {n}    The preceding item is matched exactly n times.

-------------------------------------------------------------------------------


Search words only -w [not inword]

grep -w "word" file

egrep -w 'word1 | word2' /path/to/file  [2 words with egrep]

-----------------------------------------------------------------

Does not contain word -v

grep -v word /path/to/file

--------------------------------------------
                                            |
-i Ignore case                              |
-w Match whole words                        |
-v Select non matching lines                |
-n Print Number with output lines           |
-h Supress file name prefix                 |
-r Recursive search                         |
-R as above + symbolic links   +
-o              |
 -------------------------------------------

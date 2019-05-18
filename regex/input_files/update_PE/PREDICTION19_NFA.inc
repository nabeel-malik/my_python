DATES                                  -- Generated : Petrel
  1 DEC 2016 /
  /

SKIP                                   -- Generated : Petrel
--Hint: Select wells on the input tree, drop in with the blue arrow, then add rules with the rule pop-up

ENDSKIP                                -- Generated : Petrel

WELSPECS                               -- Generated : Petrel
--'10-8' is the simulation well name used to describe flow from '10-8'
--'J-3H' is the simulation well name used to describe flow from 'J-3H'
--'10-8A' is the simulation well name used to describe flow from '10-8A'
--'J-2H' is the simulation well name used to describe flow from 'J-2H;Tubing 1'
--'J-3AH' is the simulation well name used to describe flow from 'J-3AH;Tubing 1'
--'J-1H' is the simulation well name used to describe flow from 'J-1H;Tubing 1'
--
  10-8 JP 61 43 1* OIL /
  J-3H JP 75 50 1* OIL /
  10-8A JP 60 52 1* OIL /
  J-2H JP 62 41 1* OIL /
  J-3AH JP 78 52 1* OIL /
  J-1H JI 65 55 1* WATER /
  /

WLIST                                  -- Generated : Petrel
  '*WELLS' NEW
  10-8 10-8A J-1H J-2H J-3AH J-3H /
  '*WELLS F' NEW
  10-8 10-8A J-1H J-2H J-3AH J-3H /
  /

GRUPTREE                               -- Generated : Petrel
  JP FIELD /
  JI FIELD /
  /

WELOPEN                                -- Generated : Petrel
  J-2H STOP /
  J-1H STOP /
  10-8 SHUT /
  J-3H SHUT /
  10-8A SHUT /
  J-3AH STOP /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9300{*}%PEMULT% /
  JI 0.9300{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2017 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010117% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010117% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010117% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010117% %AQPIPRED% 1 /
/
  
GEFAC                                  -- Generated : Petrel
  JP 0.9300{*}%PEMULT% /
  JI 0.9300{*}%PEMULT% /
  /
  
DATES                                  -- Generated : Petrel
  1 FEB 2017 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.8910{*}%PEMULT% /
  JI 0.8910{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 MAR 2017 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9260{*}%PEMULT% /
  JI 0.9260{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 APR 2017 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 MAY 2017 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9210{*}%PEMULT% /
  JI 0.9210{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JUN 2017 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9170{*}%PEMULT% /
  JI 0.9170{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JUL 2017 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9260{*}%PEMULT% /
  JI 0.9260{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 AUG 2017 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.8990{*}%PEMULT% /
  JI 0.8990{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 SEP 2017 /
  /
  
WELOPEN                                -- Generated : Petrel
  J-3AH OPEN /  
  /
  
WCONPROD                               -- Generated : Petrel
  J-3AH 1* ORAT 85.00 1* 1* 1* 1* 50 1* 3 150000.00 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.8820{*}%PEMULT% /
  JI 0.8820{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 OCT 2017 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 NOV 2017 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9260{*}%PEMULT% /
  JI 0.9260{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 DEC 2017 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9260{*}%PEMULT% /
  JI 0.9260{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2018 /
  /

AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010118% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010118% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010118% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010118% %AQPIPRED% 1 /
/
  
GEFAC                                  -- Generated : Petrel
  JP 0.9360{*}%PEMULT% /
  JI 0.9360{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 FEB 2018 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9090{*}%PEMULT% /
  JI 0.9090{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 MAR 2018 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 APR 2018 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9270{*}%PEMULT% /
  JI 0.9270{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 MAY 2018 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9270{*}%PEMULT% /
  JI 0.9270{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JUN 2018 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9230{*}%PEMULT% /
  JI 0.9230{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JUL 2018 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9320{*}%PEMULT% /
  JI 0.9320{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 AUG 2018 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9320{*}%PEMULT% /
  JI 0.9320{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 SEP 2018 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.8890{*}%PEMULT% /
  JI 0.8890{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 OCT 2018 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9260{*}%PEMULT% /
  JI 0.9260{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 NOV 2018 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9320{*}%PEMULT% /
  JI 0.9320{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 DEC 2018 /
  /

GEFAC                                  -- Generated : Petrel
  JP 0.9320{*}%PEMULT% /
  JI 0.9320{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2019 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010119% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010119% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010119% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010119% %AQPIPRED% 1 /
/

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2020 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010120% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010120% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010120% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010120% %AQPIPRED% 1 /
/

GEFAC                                  -- Generated : Petrel
  JP 0.8380{*}%PEMULT% /
  JI 0.8380{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2021 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010121% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010121% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010121% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010121% %AQPIPRED% 1 /
/

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2022 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010122% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010122% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010122% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010122% %AQPIPRED% 1 /
/

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2023 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010123% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010123% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010123% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010123% %AQPIPRED% 1 /
/  

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2024 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010124% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010124% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010124% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010124% %AQPIPRED% 1 /
/  

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2025 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010125% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010125% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010125% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010125% %AQPIPRED% 1 /
/  

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2026 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010126% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010126% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010126% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010126% %AQPIPRED% 1 /
/

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2027 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010127% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010127% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010127% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010127% %AQPIPRED% 1 /
/

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2028 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010128% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010128% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010128% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010128% %AQPIPRED% 1 /
/  

GEFAC                                  -- Generated : Petrel
  JP 0.8620{*}%PEMULT% /
  JI 0.8620{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2029 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010129% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010129% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010129% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010129% %AQPIPRED% 1 /
/  

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2030 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010130% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010130% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010130% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010130% %AQPIPRED% 1 /
/  

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2031 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010131% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010131% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010131% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010131% %AQPIPRED% 1 /
/  

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2032 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010132% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010132% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010132% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010132% %AQPIPRED% 1 /
/  

GEFAC                                  -- Generated : Petrel
  JP 0.8620{*}%PEMULT% /
  JI 0.8620{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2033 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010133% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010133% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010133% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010133% %AQPIPRED% 1 /
/  

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2034 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010134% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010134% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010134% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010134% %AQPIPRED% 1 /
/  

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  1 JAN 2035 /
  /
  
AQUCHWAT                               -- Generated : Petrel
1 2699 PRESSURE %AQPNOT010135% %AQPIPRED% 1 /
2 2763 PRESSURE %AQPILE010135% %AQPIPRED% 1 /
3 2775 PRESSURE %AQPTIL010135% %AQPIPRED% 1 /
4 2848 PRESSURE %AQPARE010135% %AQPIPRED% 1 /
/

GEFAC                                  -- Generated : Petrel
  JP 0.9200{*}%PEMULT% /
  JI 0.9200{*}%PEMULT% /
  /

DATES                                  -- Generated : Petrel
  31 DEC 2035 /
  /
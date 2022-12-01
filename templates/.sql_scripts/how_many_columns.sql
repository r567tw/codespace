-- https://blog.csdn.net/spurs611/article/details/88706333
SELECT 
  count(*),`table_name` 
FROM
  information_schema.COLUMNS 
WHERE table_schema = 'ear'
group by `table_name`; 
  -- AND table_name = 'dept' ;
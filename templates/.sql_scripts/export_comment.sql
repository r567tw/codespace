-- 來源: https://stackoverflow.com/questions/5404051/show-comment-of-fields-from-mysql-table
SELECT 
    `column_name` as `Field`, `column_comment` as `Comment`
FROM
    `information_schema`.`COLUMNS`
WHERE
    `table_name` = 'area_channel'
    AND `table_schema` = 'ear'
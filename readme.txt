# id and tag and category make code
## how to run python code
$ python3 main.py

## tree path txt make bash
find target_folder/ -mindepth 1 -type d | xargs -I[] bash -c "echo [] | sed -e 's/\ /\\\\\\\\\ /g' | xargs -I__ bash -c 'echo __ > __/pwd.txt'"

## cf bash example
cf1 - download1)
https://www.kosha.or.kr/extappKosha/kosha/guidance/fileDownload.do?sfhlhTchnlgyManualNo=A-193-2023&fileOrdrNo=4
cat list.txt |iconv -fcp949 | sed -e 's/.*\([A-Z]-[0-9]\{1,1000\}-[0-9]\{4\}\).*/\1/g' | xargs -I[] wget 'https://www.kosha.or.kr/extappKosha/kosha/guidance/fileDownload.do?sfhlhTchnlgyManualNo=[]&fileOrdrNo=3' -O3/[].pdf

cf2 -  디렉토리 목록을, 그안에 파일이 몇개있는지 짝짓기
ls | grep fileOrdr | xargs -I[] bash -c "paste <(echo []) <(ls [] |wc|sed -e 's/^\ \+\([0-9]\+\).*/\1/g')"

cf3 - awk 연습
cat list.txt | awk -v FS='\t' -v OFS='\t' 'match($9,/[\(|-|"]/) {print $9}'

## cf - mysql or mariadb query example
show global variables where value like '%data%';
show global variables where variable_name like '%data%';
show global variables like 'log_error';
show global variables like 'general_log';
# SET GLOBAL log_error = '/var/log/mysqld.log';
# SET GLOBAL general_log='OFF';  -- 순식간에 늘어나니 운영DB 에서는 빨리 끌것
SELECT * FROM mysql.general_log where event_time like '2024-07-02 10:%' order by event_time desc;

SELECT system('date');
SELECT system('/home/juyoung/tmp.sh');
SELECT sys_exec('tmp.sh');	# need 'lib_mysqludf_sys'
SHOW VARIABLES LIKE 'plugin_dir';

SELECT table_schema AS "Database", ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) AS "MB"
FROM information_schema.TABLES
GROUP BY 1;

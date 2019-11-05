# CCMover
To move gcc code coverage data from older branch to new branch

Multiple integrations happens daily on our project branch. If we get the code coverage data today, we will have more uncovered code available tomorrow. To leverage the code coverage data taken on Old source, we need some way to map same line, function coverage on new source.

It will need old info file, Directory where all required c file are extracted from old source without its copying its directory structure &

Directory where all required c file are extracted from old source without its copying its directory structure.

generated output will be info file which will be compatible with new source.

Extract required c files from old source:
```shell
$cd <$TOP of old tree>
$copy_source.sh <directory_name>
[Note: copy_source.sh only extracts c files required for system software & Communication Module. Edit it according to need.]
````

Extract required c files from new source:
```shell
$cd <$TOP of new tree>
$copy_source.sh <directory_name>
```

Run below command to process one old info file according to new source:
```shell
$process_info.py -i <old_info_file> -o <output_processed_file> -oc <Old c Directory> -nc <New c Directory>
```

For processing multiple file:
```shell
$for a in *.info; do process_info.py -i $a -o <processed_info_directory>/$a -oc <Old c Directory> -nc <New c Directory>; done
```

Remove data of unnecessary file in old source which is not available in new source:
```shell
$remove_oldc_info.py -i <info_file> -o <output_info>
```

For processing multiple files
```shell
$for i in *.info; do remove_oldc_info.py -i $i -o <output_info_dire>/$i; done
```
```shell
Once Processed you can gather all info file & generate report using genhtml command
$genhtml -w "$user_dirs" --frames --function-coverage -o cc_report *.info
```

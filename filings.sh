for filename in ./*.tsv; do
#	q -d"|" "SELECT * FROM $filename LIMIT 1"
	sed -i 's/\\/*/g' $filename
done

rm -rf "day$1/"
mkdir "day$1"
cp default.py "day$1/code.py"
bash getinput.sh $1
touch "day$1/test.txt"
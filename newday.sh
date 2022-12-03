rm -rf "day$1/"
mkdir "day$1"
cp default.py "day$1/main.py"
bash getinput.sh $1
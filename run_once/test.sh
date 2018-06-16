 #!/bin/sh
echo hallo ich bin ein shell script, nun nummer 2
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

echo $SCRIPTPATH

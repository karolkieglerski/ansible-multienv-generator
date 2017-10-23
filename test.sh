#!/bin/bash

tree template > test1
tree $1 > test2

diff test1 test2

rm test1 test2
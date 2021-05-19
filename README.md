# big_brain_snake

## snake game controlled by neural network trained with genetic (and biological) algorithms

### by [michlampert](http://github.com/michlampert) & [WojtAcht](http://github.com/WojtAcht) & [tmek1244](http://github.com/tmek1244)

#### Written in python, with numpy and cython features

`pip install -r requirements.txt` to install Python modules

`py setup.py build_ext --inplace` for compile map_distance module

create directory to save best brains

run `py main.py` and relax

## genetic algorithm

| <img width="1000px"> | <img width="1000px"> |
| -- | -- |
| ![rys](demos/demo_first_implementation.gif) <br/> first implementation <br/> 4x18 input neurons <br/> each generation - 1024 snakes| ![rys](logs/logs_1.png)|
| ![rys](demos/demo_second_implementation.gif) <br/> second implementation <br/> 12 input neurons with symmetry <br/> each generation - 100 snakes | ![rys](logs/logs_6.png)|
| ![rys](demos/demo_third_implementation.gif) <br/> second implementation <br/> 12 input neurons with symmetry <br/> each generation - 100 snakes <br/> crossing with mean of two genes| ![rys](logs/logs_5.png)|
| ![rys](demos/demo_fourth_implementation.gif) <br/> fourth implementation <br/> 12 input neurons with symmetry <br/> each generation - 100 snakes | ![rys](logs/logs_7.png)|


## PSO algorithm

| <img width="1000px"> | <img width="1000px"> |
| -- | -- |
| ![rys](demos/demo_PSO_1.gif) <br/> 12 input neurons with symmetry <br/> each generation - 100 snakes <br/> w=0.1 <br/> c2=0.1| ![rys](logs/logs_8.png) |
| ![rys](demos/demo_PSO_2.gif) <br/> 12 input neurons with symmetry <br/> each generation - 100 snakes <br/> w=0.05 <br/> c2=0.2 | ![rys](logs/logs_9.png) |
| ![rys](demos/demo_PSO_3.gif) <br/> 12 input neurons with symmetry <br/> each generation - 100 snakes <br/> w=0.2 <br/> c2=0.05 | ![rys](logs/logs_10.png) |
| ![rys](demos/demo_PSO_4.gif) <br/> 12 input neurons with symmetry <br/> each generation - 100 snakes <br/> w=0.1 <br/> c2=0.05 | ![rys](logs/logs_11.png) |


## Human and random input

| <img width="1000px"> | <img width="1000px"> |
| -- | -- |
| snake with human input <br/> ![rys](demos/demo.gif) | snake with random moves <br/> ![rys](demos/demo1.gif) |




## PSO algorithm

| <img width="1000px"> | <img width="1000px"> | <img width="1000px"> | <img width="1000px"> |
| -- | -- | -- | -- |
| ![rys](demos/demo_PSO_1.gif) | ![rys](logs/logs_8.png) |
| ![rys](demos/demo_PSO_2.gif) | ![rys](logs/logs_9.png) |
| ![rys](demos/demo_PSO_3.gif) | ![rys](logs/logs_10.png) |
| ![rys](demos/demo_PSO_4.gif) | ![rys](logs/logs_11.png) |



{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "Defines two dictionaries for converting \n",
    "between text and integer sequences.\n",
    "\"\"\"\n",
    "\n",
    "char_map_str = \"\"\"\n",
    "' 0\n",
    "<SPACE> 1\n",
    "a 2\n",
    "b 3\n",
    "c 4\n",
    "d 5\n",
    "e 6\n",
    "f 7\n",
    "g 8\n",
    "h 9\n",
    "i 10\n",
    "j 11\n",
    "k 12\n",
    "l 13\n",
    "m 14\n",
    "n 15\n",
    "o 16\n",
    "p 17\n",
    "q 18\n",
    "r 19\n",
    "s 20\n",
    "t 21\n",
    "u 22\n",
    "v 23\n",
    "w 24\n",
    "x 25\n",
    "y 26\n",
    "z 27\n",
    "\"\"\"\n",
    "# the \"blank\" character is mapped to 28\n",
    "\n",
    "char_map = {}\n",
    "index_map = {}\n",
    "for line in char_map_str.strip().split('\\n'):\n",
    "    ch, index = line.split()\n",
    "    char_map[ch] = int(index)\n",
    "    index_map[int(index)+1] = ch\n",
    "index_map[2] = ' '"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

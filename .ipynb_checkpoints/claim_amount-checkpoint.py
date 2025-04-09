{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f578d99e-a2eb-490e-89c4-6cf9d66fc799",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pydantic import BaseModel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3e680e42-fe9e-49b2-893c-9f5bebd92b32",
   "metadata": {},
   "outputs": [],
   "source": [
    "class claim(BaseModel):\n",
    "    wind:float\n",
    "    rain:float\n",
    "    area:float"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93649106-71cb-4f1a-8474-2e578eb81a69",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8e10e9cd",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-03-29T15:43:24.519721Z",
     "iopub.status.busy": "2023-03-29T15:43:24.518876Z",
     "iopub.status.idle": "2023-03-29T15:43:24.533128Z",
     "shell.execute_reply": "2023-03-29T15:43:24.531899Z"
    },
    "papermill": {
     "duration": 0.021512,
     "end_time": "2023-03-29T15:43:24.535903",
     "exception": false,
     "start_time": "2023-03-29T15:43:24.514391",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Factorial\n",
    "def factorial(n):\n",
    "    fac = 1\n",
    "    for i in range(1, n+1):\n",
    "        fac *= i    \n",
    "    return fac\n",
    "\n",
    "# Kombinasi\n",
    "def kombinasi(n, x):\n",
    "    comb = factorial(n)/(factorial(x) * factorial(n - x))\n",
    "    return comb\n",
    "\n",
    "# Permutasi\n",
    "def permutasi(n, x):\n",
    "    perm = factorial(n)/factorial(n - x)\n",
    "    return perm\n",
    "\n",
    "# Permutasi Siklis\n",
    "def siklis(n):\n",
    "    return factorial(n-1)\n",
    "\n",
    "# Binomial Expansion\n",
    "def binom_exp(n, r, a, b):\n",
    "    coef = kombinasi(n, r) * (a**r) * (b**(n-r))\n",
    "    return coef"
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
   "version": "3.7.12"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 12.055305,
   "end_time": "2023-03-29T15:43:25.361239",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2023-03-29T15:43:13.305934",
   "version": "2.4.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

# OMR-sheet-processing
GSIH 2024
Problem Statement:
You are given an image representing a scanned OMR answer sheet. Each image contains a grid of circles, with each row representing one question and each column representing a possible answer (A, B, C, D). Some circles are filled to indicate the selected answer by the candidate.

Your task is to write a program that takes the image as input, along with an array containing the correct answers for each question and returns a score based on the number of correct answers. For each correct answer, score will be incremented by 1 point. Each question has only 1 correct answer.

The filled circles in the images can be either fully filled (360 degrees filled) or partially filled. A fully filled circle represents a definite answer, while a partially filled circle represents a probable answer. If a circle is filled more than 75% (270 degrees filled) of the area, it should be considered as a definite answer.

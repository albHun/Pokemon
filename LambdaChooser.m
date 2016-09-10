% initializtion
clear ; close all; clc

% load TraningData and CV data
TraningData = load("TraningSet.txt");
CrossValidationData = load("CrossValidationSet.txt");

% extract X and y and Xval and yval
X = TraningData(:, 1:end-1);
y = TraningData(:, end);
Xval = CrossValidationData(:, 1:end-1);
yval = CrossValidationData(:, end);

% train linear regression with multiple lambda values
lambda_vec = [0.01, 0.03, 0.1, 0.3, 1, 3, 10];
for i = 1:length(lambda_vec)
  [theta] = trainLinearReg([ones(size(X, 1), 1) X], y, lambda_vec(i));
  [J, grad] = linearRegCostFunction([ones(size(X, 1), 1) X], y, theta, lambda_vec(i));
  disp("Lambda: "), disp(lambda_vec(i));
  disp("Cost in training set: "), disp(J);
  [J, grad] = linearRegCostFunction([ones(size(Xval, 1), 1) Xval], yval, theta, lambda_vec(i));
  disp("Cost in cross validation set: "), disp(J);
endfor
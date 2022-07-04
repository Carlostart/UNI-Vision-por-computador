%--------------------------------------------------------------------------
%                    EXERCISE: BAYESIAN CLASSIFIER
%--------------------------------------------------------------------------

function exercise_bayesian_clasifier

% Clean the workspace
close all;
clear variables;

% Control the execution of certain parts of the exercise
execute_classification = 1;
execute_boundaries     = 1;

% Load bottle images from file and store their Hu moments
N_bottles = 15;
N_bottle_types = 3;
Bottle_types = {'botella_A_','botella_B_','botella_C_'};
types = ['A','B','C'];

for type = 1:3
   for i_bottle = 1:N_bottles
       im_file_name = strcat(Bottle_types(type),int2str(i_bottle),'.bmp'); 
       im = imread(im_file_name{1});
       MHu(i_bottle,:,type) = momentos_Hu(im);
   end
end

% Show the first two moments for the images of each type
figure()
hold on;
title('Bayesian classifier')
plot (MHu(:,1,1),MHu(:,2,1),'b*')
plot (MHu(:,1,2),MHu(:,2,2),'rx')
plot (MHu(:,1,3),MHu(:,2,3),'go')

% Compute their mean and show the centroids of the two first Hu moments
centroids = [[sum(MHu(:,1,1))/length(MHu(:,1,1)) sum(MHu(:,2,1))/length(MHu(:,2,1))] 
    [sum(MHu(:,1,2))/length(MHu(:,1,2)) sum(MHu(:,2,2))/length(MHu(:,2,2))] 
    [sum(MHu(:,1,3))/length(MHu(:,1,3)) sum(MHu(:,2,3))/length(MHu(:,2,3))]];

plot (centroids(1,1), centroids(1,2),'ks','MarkerSize',8,'MarkerFaceColor','b')
text (centroids(1,1) + 0.02, centroids(1,2),'Centroid of bottle type A','Color','blue')

plot (centroids(2,1), centroids(2,2),'ks','MarkerSize',8,'MarkerFaceColor','r')
text (centroids(2,1) + 0.02, centroids(2,2),'Centroid of bottle type B','Color','red')

plot (centroids(3,1), centroids(3,2),'ks','MarkerSize',8,'MarkerFaceColor','g')
text (centroids(3,1) + 0.02, centroids(3,2),'Centroid of bottle type C','Color','green')

% Compute their covariance matrices and show them
for bt = 1:1:N_bottle_types
    covars(:,:,bt) = cov(MHu(:,1,bt),MHu(:,2,bt));
    error_ellipse(covars(:,:,bt)*10,centroids(bt,:));
end

if execute_classification == 1
    %Ok, now load the bottles not used for training, and classify them using
    % a Bayesian classifier

    N_starting_bottle = N_bottles+1;
    N_bottles = 5;

    for type = 1:3
       for i_bottle = N_starting_bottle:N_starting_bottle+N_bottles-1
           im_file_name = strcat(Bottle_types(type),int2str(i_bottle),'.bmp'); 
           im = imread(im_file_name{1});
           MHu_to_classify(i_bottle,:,type) = momentos_Hu(im);
           features = MHu_to_classify(i_bottle,:,type);

           % Call the three decisions functions
           d1 = evaluateDecisionFunction(features, 3, centroids(1,:),covars(:,:,1),1/3);
           d2 = evaluateDecisionFunction(features, 3, centroids(2,:),covars(:,:,2),1/3);
           d3 = evaluateDecisionFunction(features, 3, centroids(3,:),covars(:,:,3),1/3);

           % Get the winner!
           m=max([d1 d2 d3]);
           if m==d1
               classified_as = 1;
           elseif m==d2
               classified_as = 2;
           else
               classified_as = 3;
           end

           % Show graphically the results
           res = sprintf('Classified as: %c\n', types(classified_as));
           handler1 = plot(MHu_to_classify(i_bottle,1,type), MHu_to_classify(i_bottle,2,type),'dc','MarkerSize',10);
           handler2 = text(MHu_to_classify(i_bottle,1,type) + 0.01, MHu_to_classify(i_bottle,2,type) + 0.01,res);
           pause

           delete(handler1);
           delete(handler2);
       end
    end
end

if execute_boundaries == 1
    % Plot the decision boundary between all the possible pairs of bottle
    % types: AB, AC and BC.
    % First, get the matrix representing each conic section
    conic_matrix_A = get_conic_matrix(covars(:,:,1),centroids(1,:));
    conic_matrix_B = get_conic_matrix(covars(:,:,2),centroids(2,:));
    conic_matrix_C = get_conic_matrix(covars(:,:,3),centroids(3,:));
    disp(conic_matrix_A);
    % Get decision boundary between all the types (their conic section 
    % representation)
    decision_boundaryAB = conic_matrix_A - conic_matrix_B;
    decision_boundaryAC = conic_matrix_A - conic_matrix_C;
    decision_boundaryBC = conic_matrix_B - conic_matrix_C;
    
    % Plot them using plotConic
    plotConic(decision_boundaryAB, 'm');
    plotConic(decision_boundaryAC, 'k');
    plotConic(decision_boundaryBC, 'r');
end

end

function d = evaluateDecisionFunction(x, num_classes, mu, covar, prior)
    % Evaluate the gaussian deccision function of a vector of features given:
    % x: vector of features
    % num_classes: number of classes in the problem
    % covar: covariance matrix of the class
    % prior: a priori probability of that class
    d = log(prior) + log(1/(((2*pi)^(num_classes/2))*((det(covar)^1/2)))*exp((-1/2)*((x(1:2)-mu)*inv(covar))*transpose(x(1:2)-mu)));
end
function conic_matrix = get_conic_matrix(covariance,centroid)
% Returns the matrix representation of a conic section given the:
% covariance: covariance matrix of a two dimensional gaussian
% centoid: centroid [mu1 mu2] of that gaussian
    syms x1 x2
    X = [x1 x2];
    independiente = -1/2*((log(det(covariance))+centroid*covariance.^(-1)*centroid'));
    lineal = X*covariance.^(-1)*centroid'; % simplify?
    cuadratico = -1/2*X*covariance.^(-1)*X.';
    ecuacion = cuadratico + lineal + independiente;
    [decision,terminos] = coeffs(ecuacion);
    A = double(decision(find(terminos==x1^2)));
    B = double(decision(find(terminos==x1*x2)));
    C = double(decision(find(terminos==x2^2)));
    D = double((decision(find(terminos==x1))));
    E = double(decision(find(terminos==x2)));
    F = double(decision(find(terminos==1)));
    conic_matrix = [A B/2 D/2; B/2 C E/2; D/2 E/2 F];
end

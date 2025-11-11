def binary_classification_metrics(prediction, ground_truth):

    from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

    
    accuracy = accuracy_score(ground_truth, prediction)
    precision = precision_score(ground_truth, prediction)  
    recall = recall_score(ground_truth, prediction)
    f1 = f1_score(ground_truth, prediction)

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    
    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    return 0

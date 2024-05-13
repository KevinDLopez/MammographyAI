import matplotlib.pyplot as plt 
from typing import List, Tuple, TypedDict, Dict

def plot_histories(histories:List[ Dict[str, List[int]]], log_scale=False):
    '''Plot the training and validation loss and accuracy of the models in the histories list
    histories: List of histories dictionaries
    '''
    plt.figure(figsize=(10, 15))
    
    history_dictionary : Dict[str, List[int] ]  = {}
    # make a whole array from the elements of the dictionary 
    for history in histories:
        for plt_name, values in history.items():
            if plt_name not in history_dictionary:
                history_dictionary[plt_name] = []
            history_dictionary[plt_name].extend(values) 
   
    
    plt.subplot(len(history_dictionary)//2,1,1)
    plt.title('Loss')
    plt.plot(history_dictionary['loss'], label='Training Loss')
    plt.plot(history_dictionary['val_loss'], label='Validation Loss')
    if log_scale:
        plt.yscale("log")
    plt.legend()

    plt.subplot(len(history_dictionary)//2,1,2)
    plt.title('Accuracy')
    plt.plot(history_dictionary['accuracy'], label='Training Accuracy')
    plt.plot(history_dictionary['val_accuracy'], label='Validation Accuracy')
    if log_scale:
        plt.yscale("log")
    plt.legend()

    plt.subplot(len(history_dictionary)//2,1,3)
    plt.title("Recall")
    plt.plot(history_dictionary['recall'], label='Training Recall')
    plt.plot(history_dictionary['val_recall'], label='Validation Recall')
    if log_scale:
        plt.yscale("log")
    plt.legend()

    if "precision" in history_dictionary:
        plt.subplot(len(history_dictionary)//2,1,4)
        plt.title("precision")
        plt.plot(history_dictionary['precision'], label='Training precision')
        plt.plot(history_dictionary['val_precision'], label='Validation precision')
        if log_scale:
            plt.yscale("log")
        plt.legend()

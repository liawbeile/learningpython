def char_frequency(the_sentence):
    freq_dict={}
    for character in the_sentence:
        if character in freq_dict:
            freq_dict[character]=freq_dict[character]+1
        else:
            freq_dict[character]=1
    return freq_dict
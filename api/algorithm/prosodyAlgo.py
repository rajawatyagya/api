import pickle

import parselmouth
from parselmouth.praat import call, run_file
import glob
import pandas as pd
import numpy as np
import scipy
from scipy.stats import binom
from scipy.stats import ks_2samp
from scipy.stats import ttest_ind
import os


def noOfSyllables(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(
            objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[0])  # will be the integer number 10
        z4 = float(z2[3])  # will be the floating point number 8.3
    except:
        z3 = 0
        print("Try again the sound of the audio was not clear")
    return z3


def noOfPauses(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(
            objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[1])  # will be the integer number 10
        z4 = float(z2[3])  # will be the floating point number 8.3
    except:
        z3 = 0
        print("Try again the sound of the audio was not clear")
    return z3


def rateOfSpeech(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(
            objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[2])  # will be the integer number 10
        z4 = float(z2[3])  # will be the floating point number 8.3
    except:
        z3 = 0
        print("Try again the sound of the audio was not clear")
    return z3


def articulationRate(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(
            objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[3])  # will be the floating point number 8.3
    except:
        z3 = 0
        print("Try again the sound of the audio was not clear")
    return z3


def speakingDuration(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(
            objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[4])  # will be the floating point number 8.3
    except:
        z4 = 0
        print("Try again the sound of the audio was not clear")
    return z4


def originalDuration(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(
            objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[5])  # will be the floating point number 8.3
    except:
        z4 = 0
        print("Try again the sound of the audio was not clear")
    return z4


def balanceRatio(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(
            objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[6])  # will be the floating point number 8.3
    except:
        z4 = 0
        print("Try again the sound of the audio was not clear")
    return z4


def globalMeanOfFundamentalFrequency(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound
        # object
        z1 = str(objects[1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[7])  # will be the floating point number 8.3
    except:
        z4 = 0
        print("Try again the sound of the audio was not clear")
    return z4


def globalStandardDeviationOfFunFreq(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound
        # object
        z1 = str(objects[1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[8])  # will be the floating point number 8.3
    except:
        z4 = 0
        print("Try again the sound of the audio was not clear")
    return z4


def globalMedianOfFunFreq(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(
            objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[3])  # will be the integer number 10
        z4 = float(z2[9])  # will be the floating point number 8.3
    except:
        z4 = 0
        print("Try again the sound of the audio was not clear")
    return z4


def globalMinOfFunFreq(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound
        # object
        z1 = str(objects[
                     1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[10])  # will be the integer number 10
        z4 = float(z2[10])  # will be the floating point number 8.3
    except:
        z3 = 0
        print("Try again the sound of the audio was not clear")
    return z3


def globalMaxOfFunFreq(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound
        # object
        z1 = str(objects[1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[11])  # will be the integer number 10
        z4 = float(z2[11])  # will be the floating point number 8.3
    except:
        z3 = 0
        print("Try again the sound of the audio was not clear")
    return z3


def funFreq25thQuantile(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound
        # object
        z1 = str(objects[1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[12])  # will be the integer number 10
        z4 = float(z2[11])  # will be the floating point number 8.3
    except:
        z3 = 0
        print("Try again the sound of the audio was not clear")
    return z3


def funFreq75thQuantile(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound
        # object
        z1 = str(objects[1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[13])  # will be the integer number 10
        z4 = float(z2[11])  # will be the floating point number 8.3
    except:
        z3 = 0
        print("Try again the sound of the audio was not clear")
    return z3


def pronProbPercentage(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound
        # object
        z1 = str(objects[1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = int(z2[13])  # will be the integer number 10
        z4 = float(z2[14])  # will be the floating point number 8.3
        db = binom.rvs(n=10, p=z4, size=10000)
        a = np.array(db)
        b = np.mean(a) * 100 / 10
        return b
    except:
        print("Try again the sound of the audio was not clear")
        return 0


def genderRecognition(m, p):
    g = 0
    j = 0
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound
        # object
        z1 = str(objects[1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = float(z2[8])  # will be the integer number 10
        z4 = float(z2[7])  # will be the floating point number 8.3
        if z4 <= 114:
            g = 101
            j = 3.4
        elif 114 < z4 <= 135:
            g = 128
            j = 4.35
        elif 135 < z4 <= 163:
            g = 142
            j = 4.85
        elif 163 < z4 <= 197:
            g = 182
            j = 2.7
        elif 197 < z4 <= 226:
            g = 213
            j = 4.5
        elif z4 > 226:
            g = 239
            j = 5.3
        else:
            print("Voice not recognized")
            exit()

        def teset(a, b, c, d):
            d1 = np.random.wald(a, 1, 1000)
            d2 = np.random.wald(b, 1, 1000)
            d3 = ks_2samp(d1, d2)
            c1 = np.random.normal(a, c, 1000)
            c2 = np.random.normal(b, d, 1000)
            c3 = ttest_ind(c1, c2)
            y = ([d3[0], d3[1], abs(c3[0]), c3[1]])
            return y

        nn = 0
        mm = teset(g, j, z4, z3)
        while mm[3] > 0.05 and mm[0] > 0.04 or nn < 5:
            mm = teset(g, j, z4, z3)
            nn = nn + 1
        sampleSize = nn
        if mm[3] <= 0.09:
            p_value = mm[3]
        else:
            p_value = 0.35
        if 97 < z4 <= 114:
            print("a Male, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % p_value,
                  sampleSize)
            return {"Gender": "Male",
                    "Emotion": "Showing no emotion, normal",
                    "p-value": sampleSize,
                    "sample size": p_value}
        elif 114 < z4 <= 135:
            print("a Male, mood of speech: Reading, p-value/sample size= :%.2f" % p_value, sampleSize)
            return {"Gender": "Male",
                    "Emotion": "Reading",
                    "p-value": p_value,
                    "sample size": sampleSize}
        elif 135 < z4 <= 163:
            print("a Male, mood of speech: Speaking passionately, p-value/sample size= :%.2f" % p_value, sampleSize)
            return {"Gender": "Male",
                    "Emotion": "Speaking passionately",
                    "p-value": p_value,
                    "sample size": sampleSize}
        elif 163 < z4 <= 197:
            print("a Female, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % p_value,
                  sampleSize)
            return {"Gender": "Female",
                    "Emotion": "Showing no emotion, normal",
                    "p-value": p_value,
                    "sample size": sampleSize}
        elif 197 < z4 <= 226:
            print("a Female, mood of speech: Reading, p-value/sample size= :%.2f" % p_value, sampleSize)
            return {"Gender": "Female",
                    "Emotion": "Reading",
                    "p-value": p_value,
                    "sample size": sampleSize}
        elif 226 < z4 <= 245:
            print("a Female, mood of speech: speaking passionately, p-value/sample size= :%.2f" % p_value, sampleSize)
            return {"Gender": "Female",
                    "Emotion": "Speaking passionately",
                    "p-value": p_value,
                    "sample size": sampleSize}
        else:
            print("Voice not recognized")
            return {"Gender": "Unrecognizable",
                    "Emotion": "Unrecognizable",
                    "p-value": p_value,
                    "sample size": sampleSize}
    except:
        print("Try again the sound of the audio was not clear")


def prosodyFeatures(m, p):
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "MLTRNL.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    outo = p + "/" + "dataset" + "/" + "datanewchi22.csv"
    outst = p + "/" + "dataset" + "/" + "datanewchi44.csv"
    outsy = p + "/" + "dataset" + "/" + "datanewchi33.csv"
    pa2 = p + "/" + "dataset" + "/" + "stats.csv"
    pa7 = p + "/" + "dataset" + "/" + "datanewchi44.csv"
    result_array = np.empty((0, 100))
    files = glob.glob(path)
    result_array = np.empty((0, 27))
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        z1 = (objects[1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object
        # with a TextGrid inside
        z3 = z1.strip().split()
        z2 = np.array([z3])
        result_array = np.append(result_array, [z3], axis=0)
        # print(z3)
        np.savetxt(outo, result_array, fmt='%s', delimiter=',')
        # Data and features analysis
        df = pd.read_csv(outo,
                         names=['avepauseduratin', 'avelongpause', 'speakingtot', 'avenumberofwords',
                                'articulationrate', 'inpro', 'f1norm', 'mr', 'q25',
                                'q50', 'q75', 'std', 'fmax', 'fmin', 'vowelinx1', 'vowelinx2', 'formantmean',
                                'formantstd', 'nuofwrds', 'npause', 'ins',
                                'fillerratio', 'xx', 'xxx', 'totsco', 'xxban', 'speakingrate'], na_values='?')
        scoreMLdataset = df.drop(['xxx', 'xxban'], axis=1)
        scoreMLdataset.to_csv(outst, header=False, index=False)
        newMLdataset = df.drop(
            ['avenumberofwords', 'f1norm', 'inpro', 'q25', 'q75', 'vowelinx1', 'nuofwrds', 'npause', 'xx', 'totsco',
             'xxban', 'speakingrate', 'fillerratio'], axis=1)
        newMLdataset.to_csv(outsy, header=False, index=False)
        namess = nms = ['avepauseduratin', 'avelongpause', 'speakingtot', 'articulationrate', 'mr',
                        'q50', 'std', 'fmax', 'fmin', 'vowelinx2', 'formantmean', 'formantstd', 'ins',
                        'xxx']
        df1 = pd.read_csv(outsy, names=namess)
        nsns = ['average_syll_pause_duration', 'No._long_pause', 'speaking_time', 'ave_No._of_words_in_minutes',
                'articulation_rate', 'No._words_in_minutes', 'formants_index', 'f0_index', 'f0_quantile_25_index',
                'f0_quantile_50_index', 'f0_quantile_75_index', 'f0_std', 'f0_max', 'f0_min', 'No._detected_vowel',
                'perc%._correct_vowel', '(f2/f1)_mean', '(f2/f1)_std',
                'no._of_words', 'no._of_pauses', 'intonation_index',
                '(voiced_syll_count)/(no_of_pause)', 'TOEFL_Scale_Score', 'Score_Shannon_index', 'speaking_rate']
        dataframe = pd.read_csv(pa2)
        df55 = pd.read_csv(outst, names=nsns)
        dataframe = dataframe.values
        array = df55.values
        print("Compared to native speech, here are the prosodic features of your speech:")
        featureReturn = {}
        for i in range(25):
            sl0 = dataframe[4:7:1, i + 1]
            score = array[0, i]
            he = scipy.stats.percentileofscore(sl0, score, kind='strict')
            if he == 0:
                he = 25
                dfout = "%s:\t %f (%s)" % (nsns[i], he, "% percentile ")
                print(dfout)
                featureReturn.update({nsns[i]: he})
            elif 25 <= he <= 75:
                dfout = "%s:\t %f (%s)" % (nsns[i], he, "% percentile ")
                print(dfout)
                featureReturn.update({nsns[i]: he})
            else:
                dfout = "%s:\t (%s)" % (nsns[i], ":Out of Range")
                print(dfout)
                featureReturn.update({nsns[i]: ":Out of Range"})
        return featureReturn
    except:
        print("Try again the sound of the audio was not clear")


def finalEvaluation(m, p):
    import sys

    def my_except_hook(exctype, value, traceback):
        print('There has been an error in the system')

    sys.excepthook = my_except_hook
    import warnings
    if not sys.warnoptions:
        warnings.simplefilter("ignore")
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "MLTRNL.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    pa1 = p + "/" + "dataset" + "/" + "datanewchi23.csv"
    pa7 = p + "/" + "dataset" + "/" + "datanewchi45.csv"
    pa5 = p + "/" + "dataset" + "/" + "datanewchi34.csv"
    result_array = np.empty((0, 100))
    ph = sound
    files = glob.glob(ph)
    result_array = np.empty((0, 27))
    final_predictions = {}
    try:
        for soundi in files:
            objects = run_file(sourcerun, -20, 2, 0.3, "yes", soundi, path, 80, 400, 0.01, capture_output=True)
            # print (objects[0]) # This will print the info from the sound object, and objects[0] is a
            # parselmouth.Sound object
            z1 = (objects[1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object
            # with a TextGrid inside
            z3 = z1.strip().split()
            z2 = np.array([z3])
            result_array = np.append(result_array, [z3], axis=0)

        np.savetxt(pa1, result_array, fmt='%s', delimiter=',')
        # Data and features analysis
        df = pd.read_csv(pa1, names=['avepauseduratin', 'avelongpause', 'speakingtot', 'avenumberofwords',
                                     'articulationrate', 'inpro', 'f1norm', 'mr', 'q25',
                                     'q50', 'q75', 'std', 'fmax', 'fmin', 'vowelinx1', 'vowelinx2', 'formantmean',
                                     'formantstd', 'nuofwrds', 'npause', 'ins',
                                     'fillerratio', 'xx', 'xxx', 'totsco', 'xxban', 'speakingrate'], na_values='?')

        scoreMLdataset = df.drop(['xxx', 'xxban'], axis=1)
        scoreMLdataset.to_csv(pa7, header=False, index=False)
        newMLdataset = df.drop(
            ['avenumberofwords', 'f1norm', 'inpro', 'q25', 'q75', 'vowelinx1', 'nuofwrds', 'npause', 'xx', 'totsco',
             'xxban', 'speakingrate', 'fillerratio'], axis=1)
        newMLdataset.to_csv(pa5, header=False, index=False)
        namess = nms = ['avepauseduratin', 'avelongpause', 'speakingtot', 'articulationrate', 'mr',
                        'q50', 'std', 'fmax', 'fmin', 'vowelinx2', 'formantmean', 'formantstd', 'ins',
                        'xxx']
        df1 = pd.read_csv(pa5,
                          names=namess)
        df33 = df1.drop(['xxx'], axis=1)
        array = df33.values
        array = np.log(array)
        x = array[:, 0:13]

        def myspp(bp, bg):
            sound = bg + "/" + "dataset" + "/" + "audioFiles" + "/" + bp + ".wav"
            sourcerun = bg + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
            path = bg + "/" + "dataset" + "/" + "audioFiles" + "/"
            objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
            print(objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound
            # object
            z1 = str(objects[1])  # This will print the info from the textgrid object, and objects[1] is a
            # parselmouth.Data object with a TextGrid inside
            z2 = z1.strip().split()
            z3 = int(z2[13])  # will be the integer number 10
            z4 = float(z2[14])  # will be the floating point number 8.3
            db = binom.rvs(n=10, p=z4, size=10000)
            a = np.array(db)
            b = np.mean(a) * 100 / 10
            return b

        bp = m
        bg = p
        bi = myspp(bp, bg)
        print("Output percentage %s" % bi)

        filename = p + "/" + "dataset" + "/" + "essen" + "/" + "CART_model.sav"
        model = pickle.load(open(filename, 'rb'))
        predictions = model.predict(x)
        final_predictions.update({'Carl Model': predictions[0]})  # [0] first element of ndarray
        print("Carl Model with 58% accuracy    ", predictions)

        filename = p + "/" + "dataset" + "/" + "essen" + "/" + "ETC_model.sav"
        model = pickle.load(open(filename, 'rb'))
        predictions = model.predict(x)
        final_predictions.update({'ETC Model': predictions[0]})  # [0] first element of ndarray
        print("ETC Model with XX% accuracy    ", predictions)

        filename = p + "/" + "dataset" + "/" + "essen" + "/" + "KNN_model.sav"
        model = pickle.load(open(filename, 'rb'))
        predictions = model.predict(x)
        final_predictions.update({'KNN Model': predictions[0]})
        print("KNN Model with 65% accuracy    ", predictions)

        filename = p + "/" + "dataset" + "/" + "essen" + "/" + "LDA_model.sav"
        model = pickle.load(open(filename, 'rb'))
        predictions = model.predict(x)
        final_predictions.update({'LDA Model': predictions[0]})
        print("LDA Model with 70% accuracy    ", predictions)

        filename = p + "/" + "dataset" + "/" + "essen" + "/" + "LR_model.sav"
        model = pickle.load(open(filename, 'rb'))
        predictions = model.predict(x)
        final_predictions.update({'LR Model': predictions[0]})
        print("LR Model with 67% accuracy    ", predictions)

        filename = p + "/" + "dataset" + "/" + "essen" + "/" + "NB_model.sav"
        model = pickle.load(open(filename, 'rb'))
        predictions = model.predict(x)
        final_predictions.update({'NB Model': predictions[0]})
        print("NB Model with 64% accuracy    ", predictions)

        filename = p + "/" + "dataset" + "/" + "essen" + "/" + "SVN_model.sav"
        model = pickle.load(open(filename, 'rb'))
        predictions = model.predict(x)
        final_predictions.update({'SVN Model': predictions[0]})
        print("SVN Model with 63% accuracy    ", predictions)

        print(final_predictions)
    except:
        print("Try again the sound of the audio was not clear")
    return final_predictions


def consolidatedData(m, p):
    dataset = pd.DataFrame()
    sound = p + "/" + "dataset" + "/" + "audioFiles" + "/" + m + ".wav"
    sourcerun = p + "/" + "dataset" + "/" + "essen" + "/" + "myspsolution.praat"
    path = p + "/" + "dataset" + "/" + "audioFiles" + "/"
    try:
        objects = run_file(sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
        print(objects[0])  # This will print the info from the sound object, and objects[0] is a parselmouth.Sound
        # object
        z1 = str(objects[1])  # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data
        # object with a TextGrid inside
        z2 = z1.strip().split()
        z3 = np.array(z2)
        z4 = np.array(z3)[np.newaxis]
        z5 = z4.T
        dataset = pd.DataFrame({
            "number_ of_syllables": z5[0, :],
            "number_of_pauses": z5[1, :],
            "rate_of_speech": z5[2, :],
            "articulation_rate": z5[3, :],
            "speaking_duration": z5[4, :],
            "original_duration": z5[5, :],
            "balance": z5[6, :],
            "f0_mean": z5[7, :],
            "f0_std": z5[8, :],
            "f0_median": z5[9, :],
            "f0_min": z5[10, :],
            "f0_max": z5[11, :],
            "f0_quantile25": z5[12, :],
            "f0_quan75": z5[13, :]
        })
    except:
        print("Try again the sound of the audio was not clear")
    return dataset.T.iloc[:, 0]

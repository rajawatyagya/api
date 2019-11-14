import os

from rest_framework.utils import json

from api.algorithm import prosodyAlgo as ms
from iboxz.settings import BASE_DIR

path_to_my_prosody = os.path.join(BASE_DIR, 'api', 'algorithm', 'audioData', 'myprosody')


def pronunciationService(audio_file_name):
    responseData = {}
    responseData.update({"Consolidated Data": ms.consolidatedData(audio_file_name, path_to_my_prosody).to_dict()})
    responseData.update({"Pronunciation Probability": ms.pronProbPercentage(audio_file_name, path_to_my_prosody)})
    responseData.update({"Features": ms.prosodyFeatures(audio_file_name, path_to_my_prosody)})
    responseData.update({"Gender Recognition": ms.genderRecognition(audio_file_name, path_to_my_prosody)})
    responseData.update({"Final Evaluation": ms.finalEvaluation(audio_file_name, path_to_my_prosody)})
    return responseData

import image_recog

test_reco = image_recog.Image_recog("data/carla1.png",
                                    "data/carla_smile.jpg",
                                    "data/carla_not_smile.jpg")
print(test_reco.is_similar())
#print(test_reco.similarity)
print(test_reco.is_similar())
#print(test_reco.is_smiling)

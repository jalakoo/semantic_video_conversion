import cv2
import edgeiq
"""
Use semantic segmentation to determine a class for each pixel of an image.
The classes of objects detected can be changed by selecting different models.
This particular starter application uses a model on the cityscape
dataset (https://www.cityscapes-dataset.com/).
The Cityscapes Dataset focuses on semantic understanding of urban street scenes,
and is a favorite dataset for building autonomous car machine learning models.

Different images can be used by updating the files in the *images/*
directory. Note that when developing for a remote device, removing
images in the local *images/* directory won't remove images from the
device. They can be removed using the `aai app shell` command and
deleting them from the *images/* directory on the remote device.

To change the computer vision model, follow this guide:
https://dashboard.alwaysai.co/docs/application_development/changing_the_model.html

To change the engine and accelerator, follow this guide:
https://dashboard.alwaysai.co/docs/application_development/changing_the_engine_and_accelerator.html
"""


def main():
    semantic_segmentation = edgeiq.SemanticSegmentation(
            "alwaysai/enet")
    semantic_segmentation.load(engine=edgeiq.Engine.DNN)
    print('Outside of try')
    try:
        with edgeiq.FileVideoStream("driving_downtown.mp4", play_realtime=False) as video_stream, \
            edgeiq.VideoWriter(output_path="output.avi") as video_writer:
            print('Inside of try')

            if video_stream is None:
                print('no video stream!')
            else:
                print('video stream available of type {}'.format(type(video_stream)))

            if video_writer is None:
                print('no video writer!')
            else:
                print('video writer available of type {}'.format(type(video_writer)))

            more = getattr(video_stream, "more", None)
            if callable(more):
                print('video_stream has an attribute called more')
            else:
                print('video_stream has no MORE function!?')
            if video_stream.more():
                print('At least one video frame available before we bgin')

            while video_stream.more():
                print('Inside of while')
                # image = video_stream.read()
                # # video_writer.write_frame(image)
                # if image is None:
                #     print('no image')
                # else:
                #     print('image available of type {}'.format(type(image)))
                # results = semantic_segmentation.segment_image(image)
                # if results is None:
                #     print('no results')
                # else:
                #     print('results available of type {}'.format(type(results)))
                # mask = semantic_segmentation.build_image_mask(results.class_map)
                # if mask is None:
                #     print('no mask')
                # else:
                #     print('mask available of type {}'.format(type(mask)))
                # blended = edgeiq.blend_images(image, mask, alpha=0.5)
                # if blended is None:
                #     print('no blended')
                # else:
                #     print('blended available of type {}'.format(type(blended)))
                # video_writer.write_frame(image)

    finally:
        print("Program Ending")


if __name__ == "__main__":
    main()

import cv2
import os
import pickle

video_dir = '../Videos/01/'
video_index = 0
sample_rate = 6

videos = sorted(os.listdir(video_dir))
videos = [x for x in videos if not x.startswith('.')]
print('Videos in directory: {}'.format(videos))

video = os.path.join(video_dir, videos[video_index])
print("Labeling video: {}".format(video))

cap = cv2.VideoCapture(video)
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)

# load existing labels if they exist
data_files = os.listdir('labels')
data_files = [x for x in data_files if x.endswith('pkl')]
data_file = [x for x in data_files if videos[video_index].split('.')[0] in x]
if len(data_file) == 1:
    labels = pickle.load(open('labels/{}'.format(data_file[0]), 'rb'))
    labeled_frames = list(labels.keys())
    i = labeled_frames[-1] + sample_rate
    print('Frames labeled: {}/{}'.format(int((i - sample_rate) / sample_rate), int(frames / sample_rate)))
else:
    labels = {}
    i = 0
    print('Frames labeled: 0/{}'.format(int(frames / sample_rate)))

winname = videos[video_index]
cv2.namedWindow(winname)
while i < int(frames):
    if i % sample_rate == 0:
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, img = cap.read()
        if ret:
            if i in labels.keys():
                label_txt = labels[i]
            else:
                label_txt = None
            cv2.putText(img, 'Frame {}/{} Label: {}'.format(i, int(frames), label_txt),
                        org=(10,20), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.75, color=(255, 255, 0))
            cv2.imshow(winname, img)
            key = cv2.waitKey(0)

            if key == ord('q'):  # quit
                cv2.destroyAllWindows()
                break

            if key == ord('.'):  # next frame
                i += 1

            if key == ord(','):  # previous frame
                if i > 0:
                    i -= sample_rate
            if key == ord('1'):
                labels[i] = 'ISTD'
                pickle.dump(labels, open('./labels/{}.pkl'.format(videos[video_index].split('.')[0]), 'wb'))
                print('Saved label: {}: {}'.format(i, 'ISTD'))
                i += 1

            if key == ord('2'):
                labels[i] = 'ISTL'
                pickle.dump(labels, open('./labels/{}.pkl'.format(videos[video_index].split('.')[0]), 'wb'))
                print('Saved label: {}: {}'.format(i, 'ISTL'))
                i += 1

            if key == ord('3'):
                labels[i] = 'ISS'
                pickle.dump(labels, open('./labels/{}.pkl'.format(videos[video_index].split('.')[0]), 'wb'))
                print('Saved label: {}: {}'.format(i, 'ISS'))
                i += 1

            if key == ord('4'):
                labels[i] = 'DSTD'
                pickle.dump(labels, open('./labels/{}.pkl'.format(videos[video_index].split('.')[0]), 'wb'))
                print('Saved label: {}: {}'.format(i, 'DSTD'))
                i += 1

            if key == ord('5'):
                labels[i] = 'DSTL'
                pickle.dump(labels, open('./labels/{}.pkl'.format(videos[video_index].split('.')[0]), 'wb'))
                print('Saved label: {}: {}'.format(i, 'DSTL'))
                i += 1

            if key == ord('6'):
                labels[i] = 'DSS'
                pickle.dump(labels, open('./labels/{}.pkl'.format(videos[video_index].split('.')[0]), 'wb'))
                print('Saved label: {}: {}'.format(i, 'DSS'))
                i += 1

            if key == ord('7'):
                labels[i] = 'LTD'
                pickle.dump(labels, open('./labels/{}.pkl'.format(videos[video_index].split('.')[0]), 'wb'))
                print('Saved label: {}: {}'.format(i, 'LTD'))
                i += 1

            if key == ord('8'):
                labels[i] = 'LTO'
                pickle.dump(labels, open('./labels/{}.pkl'.format(videos[video_index].split('.')[0]), 'wb'))
                print('Saved label: {}: {}'.format(i, 'LT0'))
                i += 1

            if key == ord('9'):
                labels[i] = 'LTIS'
                pickle.dump(labels, open('./labels/{}.pkl'.format(videos[video_index].split('.')[0]), 'wb'))
                print('Saved label: {}: {}'.format(i, 'LTIS'))
                i += 1

            if key == ord('Q'):
                labels[i] = 'LTDS'
                pickle.dump(labels, open('./labels/{}.pkl'.format(videos[video_index].split('.')[0]), 'wb'))
                print('Saved label: {}: {}'.format(i, 'LTDS'))
                i += 1

            if key == ord('W'):
                labels[i] = 'LTSE'
                pickle.dump(labels, open('./labels/{}.pkl'.format(videos[video_index].split('.')[0]), 'wb'))
                print('Saved label: {}: {}'.format(i, 'LTSE'))
                i += 1

            if key == ord('E'):
                labels[i] = 'LS'
                pickle.dump(labels, open('./labels/{}.pkl'.format(videos[video_index].split('.')[0]), 'wb'))
                print('Saved label: {}: {}'.format(i, 'LS'))
                i += 1
    else:
        i += 1
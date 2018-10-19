import cv2

class Video:
    def __init__(self, video_source):
        if not video_source.isOpened():
            raise ValueError("cant connect to video source", video_source)

        self.width = video_source.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = video_source.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def update(self, video_source):
        while True:
            ret, frame = video_source.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def __del__(self):
        if video_source.isOpened():
            video_source.release()
            cv2.destroyAllWindows()

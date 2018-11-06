<<<<<<< HEAD
import cv2

class Video:
    def __init__(self, video_source):
        self.video_source = video_source
        if not self.video_source.isOpened():
            raise ValueError("cant connect to video source", video_source)

        self.width = video_source.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = video_source.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def update(self):
        while True:
            ret, frame = self.video_source.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def __del__(self):
        if self.video_source.isOpened():
            self.video_source.release()
            cv2.destroyAllWindows()
=======
import cv2

class Video:
    def __init__(self, video_source):
        self.video_source = video_source
        if not self.video_source.isOpened():
            raise ValueError("cant connect to video source", video_source)

        self.width = video_source.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = video_source.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def update(self):
        while True:
            ret, frame = self.video_source.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def __del__(self):
        if self.video_source.isOpened():
            self.video_source.release()
            cv2.destroyAllWindows()
>>>>>>> 28ac6228d3f02ed7fbaa1d93a48786ce6fa636da

from torchvision.datasets import ImageFolder
import os


class ImageFolderPath(ImageFolder):
    def __getitem__(self, index):
        path, _ = self.imgs[index]
        fn = os.path.split(path)[-1]
        ref = int(fn[:-4]) - 1
        return super(ImageFolderPath, self).__getitem__(index), ref
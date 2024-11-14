import unittest
import numpy as np
from app.utils.inference import run_inference

class TestModel(unittest.TestCase):
    def test_model_inference(self):
        # Basit bir siyah resim oluşturuyoruz
        image = np.zeros((640, 640, 3), dtype=np.uint8)
        boxes, scores, class_ids = run_inference(image)
        # Model çıktısı varsayılan olarak boş olacaktır.
        self.assertIsInstance(boxes, np.ndarray)
        self.assertIsInstance(scores, np.ndarray)
        self.assertIsInstance(class_ids, np.ndarray)

if __name__ == '__main__':
    unittest.main()

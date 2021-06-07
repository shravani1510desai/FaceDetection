import cv2
import mtcnn

def render_image(fileloc):
    face_detector = mtcnn.MTCNN()
    img = cv2.imread(fileloc)
    conf_t = 0.99

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detector.detect_faces(img_rgb)

    print(results)
    number_of_faces = 0
    for res in results:
        x1, y1, width, height = res['box']
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height

        confidence = res['confidence']
        if confidence < conf_t:
            continue
        key_points = res['keypoints'].values()

        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), thickness=1)
        cv2.putText(img, f'conf: {confidence:3f}', (x1, y1), cv2.FONT_ITALIC, 0.7, (0, 0, 255), 2)

        for point in key_points:
            cv2.circle(img, point, 1, (255, 255, 0), thickness=2)
        number_of_faces+=1

    cv2.imwrite(fileloc, img)
    return number_of_faces
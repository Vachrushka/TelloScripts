from pyzbar import pyzbar
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX


def draw_barcode(decoded, image):
    # n_points = len(decoded.polygon)
    # for i in range(n_points):
    #     image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
    tickness = 5
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                          (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                          color=(0, 255, 0),
                          thickness=tickness)
    cv2.putText(image,
                "Type: " + decoded.type,
                (decoded.rect.left, 6 * tickness + decoded.rect.top + decoded.rect.height),
                font, 1,
                (0, 255, 255),
                1,
                cv2.LINE_4)
    cv2.putText(image,
                "Data: " + str(decoded.data),
                (decoded.rect.left, 12 * tickness + decoded.rect.top + decoded.rect.height),
                font, 1,
                (0, 255, 255),
                1,
                cv2.LINE_4)
    return image


def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()

    return image


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    filter_num = 0
    filter_count = 3
    filter_variable = 1
    while True:
        # read the frame from the camera
        _, frame = cap.read()
        # decode detected barcodes & get the image
        # that is drawn
        if filter_num == 1:
            mask = cv2.inRange(frame, (0, 0, 0), (200, 200, 200))
            thresholded = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
            frame = 255 - thresholded
        elif filter_num == 2:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, frame = cv2.threshold(frame, (127+filter_variable)%255, 255, 0)

        elif filter_num == 3:
            thresh = (127+filter_variable)%255
            frame = cv2.threshold(frame, thresh, 255, cv2.THRESH_BINARY)[1]

        frame = decode(frame)
        # show the image in the window
        cv2.imshow("frame", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        elif key == ord("b"):
            filter_num += 1
            if filter_num > filter_count:
                filter_num = 0
        elif key == ord("p"):
            filter_variable+=2

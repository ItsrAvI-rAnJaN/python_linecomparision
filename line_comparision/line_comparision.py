import logging
import math

logging.basicConfig(filename='linecomparision_logs.log',
                    encoding='utf-8', level=logging.DEBUG)


class LineComparision:
    """
    class comparision define function to comare b/w geometry X-Y co-ordinate point 
    param : co-ordinate point of X-Y
    """

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def calc_line_length(self):
        """
        method: To Calculate length of X-Y cordinates of point 
        return: length of two lines
        """
        try:
            # define math formula to calculate length
            line_1_length = math.sqrt(
                (self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)

            return line_1_length

        except Exception as err:
            print(err)


def compare_line_length(line_1_length, line_2_length):
    """
    method: comparision b/w both line length
    return: greater length line 
    """
    try:
        if (line_1_length > line_2_length):
            print("line 1 is greater than line 2")

        elif (line_2_length > line_1_length):
            print("line 2 is greater than line 1")

        else:
            print("Both are Equal")

    except Exception as err:
        print(err)


if __name__ == "__main__":
    line_1 = LineComparision(2, 4, 5, 7)
    # print("length of Line1 & Line2 are :", line_1.calc_line_length())
    line_2 = LineComparision(4, 5, 6, 8)
    compare_line_length(line_1.calc_line_length(), line_2.calc_line_length())

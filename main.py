import sys
from dashborad import ai_explain

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("ERROR: Expecting Arguments")
        sys.exit(1)
    if len(sys.argv) == 3:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
    else:
        print("You have not entered all argument.Please input test data and model ==>")
        sys.exit(1)
    data_path = arg1
    model = arg2
    ai_explain(arg1,arg2)

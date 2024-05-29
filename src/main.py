"""
main.py

run all the modules
"""
from src import spiderhyl
from src import age
from src import change
from src import keyword
from src import predict
from src import region


def run():
    """
    run all the modules
    """
    spiderhyl.main()
    predict.main()
    age.main()
    region.main()
    keyword.main()
    change.main()

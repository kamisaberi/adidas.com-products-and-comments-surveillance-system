import adidas as ad
import sys
import time

if __name__ == "__main__":
    while True:
        pass

    i = 1
    # while True:
    thread1 = ad.AdidasThread(1, ad.TYPES.ITEM_LIST)
    thread1.start()
    thread1.join()
    # time.sleep(10)

    thread2 = ad.AdidasThread(2, ad.TYPES.PRODUCTS)
    thread2.start()
    thread2.join()
    # thread.join()
    # i += 1

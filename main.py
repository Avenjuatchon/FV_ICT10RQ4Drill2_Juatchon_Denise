def sample_numpy(e):
    document.getElementById('output').innerHTML = " "
    import numpy as np
    import matplotlib.pyplot as plt

    boxes = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
    sold_boxes = np.array([4, 2, 3, 4, 7, 3, 1])
    sample_graph = plt.plot(boxes, sold_boxes)
    plt.show(sample_graph)
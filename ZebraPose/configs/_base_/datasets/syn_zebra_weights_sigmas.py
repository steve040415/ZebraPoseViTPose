dataset_info = dict(
    dataset_name='syn_zebras',
    keypoint_info={
        0:
        dict(
            name='left back paw',
            id=0,
            color=[0,255,255],
            type='lower',
            swap='right back paw'),
        1:
        dict(
            name='left back knee',
            id=1,
            color=[0,255,255],
            type='lower',
            swap='right back knee'),
        2:
        dict(name='left back thigh',
             id=2,
             color=[0,255,255],
             type='lower',
             swap='right back thigh'),
        3:
        dict(name='right back paw',
             id=3,
             color=[255,0,255],
             type='lower',
             swap='left back paw'),
        4:
        dict(
            name='right back knee',
            id=4,
            color=[255,0,255],
            type='lower',
            swap='left back knee'),
        5:
        dict(
            name='right back thigh',
            id=5,
            color=[255,0,255],
            type='lower',
            swap='left back thigh'),
        6:
        dict(
            name='right front paw',
            id=6,
            color=[0,0,255],
            type='upper',
            swap='left front paw'),
        7:
        dict(
            name='right front knee',
            id=7,
            color=[0, 0,255],
            type='upper',
            swap='left front knee'),
        8:
        dict(
            name='right front thigh',
            id=8,
            color=[0, 0, 255],
            type='upper',
            swap='left front thigh'),
        9:
        dict(
            name='left front paw',
            id=9,
            color=[0,255,0],
            type='upper',
            swap='right front paw'),
        10:
        dict(
            name='left front knee',
            id=10,
            color=[0,255,0],
            type='upper',
            swap='right front knee'),
        11:
        dict(
            name='left front thigh',
            id=11,
            color=[0,255,0],
            type='upper',
            swap='right front thigh'),
        12:
        dict(
            name='tail end',
            id=12,
            color=[255, 0, 0],
            type='lower',
            swap=''),
        13:
        dict(
            name='tail base',
            id=13,
            color=[255, 0, 0],
            type='lower',
            swap=''),
        14:
        dict(
            name='right ear tip',
            id=14,
            color=[255,255,0],
            type='upper',
            swap='left ear tip'),
        15:
        dict(
            name='right ear base',
            id=15,
            color=[255,255,0],
            type='upper',
            swap='left ear base'),
        16:
        dict(
            name='left ear tip',
            id=16,
            color=[50,128,128],
            type='upper',
            swap='right ear tip'),
        17:
        dict(
            name='left ear base',
            id=17,
            color=[50,128,128],
            type='upper',
            swap='right ear base'),
        18:
        dict(
            name='right eye',
            id=18,
            color=[255,0,50],
            type='upper',
            swap='left eye'),
        19:
        dict(
            name='left eye',
            id=19,
            color=[50,0,255],
            type='upper',
            swap='right eye'),
        20:
        dict(
            name='nose',
            id=20,
            color=[125,50, 125],
            type='upper',
            swap=''),
        21:
        dict(
            name='neck start',
            id=21,
            color=[255,0, 0],
            type='upper',
            swap=''),
        22:
        dict(
            name='neck end',
            id=22,
            color=[255, 0, 0],
            type='upper',
            swap=''),
        23:
        dict(
            name='skull',
            id=23,
            color=[255, 0, 0],
            type='upper',
            swap=''),
        24:
        dict(
            name='body middle',
            id=24,
            color=[255, 0, 0],
            type='upper',
            swap=''),
        25:
        dict(
            name='back end',
            id=25,
            color=[255, 0, 0],
            type='lower',
            swap=''),
        26:
        dict(
            name='back front',
            id=26,
            color=[255, 0, 0],
            type='upper',
            swap='')
    },
    skeleton_info={
        0: dict(link=('left back paw', 'left back knee'), id=0, color=[0, 255, 255]),
        1: dict(link=('left back knee', 'left back thigh'), id=1, color=[0, 255, 255]),
        2: dict(link=('left back thigh', 'back end'), id=2, color=[0, 255, 255]),
        3: dict(link=('right back paw', 'right back knee'), id=3, color=[255, 0, 255]),
        4: dict(link=('right back knee', 'right back thigh'), id=4, color=[255, 0, 255]),
        5: dict(link=('right back thigh', 'back end'), id=5, color=[255, 0, 255]),
        6: dict(link=('right front paw', 'right front knee'), id=6, color=[255, 0, 255]),
        7: dict(link=('right front knee', 'right front thigh'), id=7, color=[255, 0, 255]),
        8: dict(link=('left front paw', 'left front knee'), id=8, color=[0, 255, 255]),
        9: dict(link=('left front knee', 'left front thigh'), id=9, color=[0, 255, 255]),
        10: dict(link=('tail end', 'tail base'), id=10, color=[0, 0, 255]),
        11: dict(link=('right ear tip', 'right ear base'), id=11, color=[255, 0, 255]),
        12: dict(link=('left ear tip', 'left ear base'), id=12, color=[0, 255, 255]),
        13: dict(link=('right ear base', 'right eye'), id=13, color=[255, 0, 255]),
        14: dict(link=('right eye', 'left eye'), id=14, color=[255, 0, 255]),
        15: dict(link=('left ear base', 'left eye'), id=15, color=[0, 255, 255]),
        16: dict(link=('right eye', 'nose'), id=16, color=[255, 0, 255]),
        17: dict(link=('left eye', 'nose'), id=17, color=[0, 255, 255]),
        18: dict(link=('right eye', 'skull'), id=18, color=[255, 0, 255]),
        19: dict(link=('left eye', 'skull'), id=19, color=[0, 255, 255]),
        20: dict(link=('nose', 'skull'), id=20, color=[0, 0, 255]),
        21: dict(link=('skull', 'neck end'), id=21, color=[0, 0, 255]),
        22: dict(link=('neck end', 'neck start'), id=22, color=[0, 0, 255]),
        23: dict(link=('neck start', 'back front'), id=23, color=[0, 0, 255]),
        24: dict(link=('back front', 'right front thigh'), id=24, color=[0, 0, 255]),
        25: dict(link=('back front', 'left front thigh'), id=25, color=[0, 0, 255]),
        26: dict(link=('back front', 'body middle'), id=26, color=[0, 0, 255]),
        27: dict(link=('body middle', 'back end'), id=27, color=[0, 0, 255]),
        28: dict(link=('back end', 'tail base'), id=28, color=[0, 0, 255]),
    },
    # joint_weights=[1.0, 1.0, 1.0, # lb paw, lb knee, lb thigh
    #                1.0, 1.0, 1.0, # rb paw, rb knee, rb thigh
    #                1.0, 1.0, 1.0, # rf paw, rf knee, rf thigh
    #                1.0, 1.0, 1.0, # lf paw, lf knee, lf thigh
    #                1.0, 1.0, # tail end, tail base
    #                1.0, 1.0, # right ear tip, right ear base
    #                1.0, 1.0, # left ear tip, left ear base
    #                1.0, 1.0, 1.0, # right eye, left eye, nose
    #                1.0, 1.0, 1.0, # neck start, neck end, skull
    #                1.0, 1.0, 1.0], # body middle, back end, back front
    joint_weights=[1.2, 1.2, 1.0, # lb paw, lb knee, lb thigh
                   1.5, 1.5, 1.0, # rb paw, rb knee, rb thigh
                   1.5, 1.5, 1.0, # rf paw, rf knee, rf thigh
                   1.2, 1.2, 1.0, # lf paw, lf knee, lf thigh
                   1.5, 0.9, # tail end, tail base
                   0.9, 0.7, # right ear tip, right ear base
                   0.9, 0.7, # left ear tip, left ear base
                   0.5, 0.5, 0.9, # right eye, left eye, nose
                   0.6, 0.6, 0.6, # neck start, neck end, skull
                   0.6, 0.6, 0.6], # body middle, back end, back front
     sigmas=[
        0.089, 0.087, 0.107, # lb paw, lb knee, lb thigh
        0.089, 0.087, 0.107, # rb paw, rb knee, rb thigh
        0.062, 0.072, 0.079, # rf paw, rf knee, rf thigh
        0.062, 0.072, 0.79, # lf paw, lf knee, lf thigh
        0.1, 0.035, # tail end, tail base
        0.05, 0.025, # right ear tip, right ear base
        0.05, 0.025, # left ear tip, left ear base
        0.025, 0.025, 0.026, # right eye, left eye, nose
        0.035, 0.035, 0.035, # neck start, neck end, skull
        0.05, 0.035, 0.035, # body middle, back end, back front
     ],

    #sigmas=[
    #    0.09, 0.09, 0.1, # lb paw, lb knee, lb thigh
    #    0.09, 0.09, 0.1, # rb paw, rb knee, rb thigh
    #    0.09, 0.09, 0.1, # rf paw, rf knee, rf thigh
    #    0.09, 0.09, 0.1, # lf paw, lf knee, lf thigh
    #    0.1, 0.035, # tail end, tail base
    #    0.05, 0.025, # right ear tip, right ear base
    #    0.05, 0.025, # left ear tip, left ear base
    #    0.025, 0.025, 0.05, # right eye, left eye, nose
    #    0.035, 0.035, 0.035, # neck start, neck end, skull
    #    0.05, 0.025, 0.025, # body middle, back end, back front
    #],
)

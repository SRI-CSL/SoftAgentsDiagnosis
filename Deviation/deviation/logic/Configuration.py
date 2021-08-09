import sys

class Configuration:

    grid_dimension = [6, 6]

    bot_count = 2
    obs_count = 1
    thing_count = bot_count + obs_count

    pt2_count = grid_dimension[0] * grid_dimension[1]
    stage_count = 5

    timeline_interpretation = 1

    INTERPRETATIONS = {
        0 : 'No assumptions on timeline timestamps',
        1 : 'Timeline timestamps are distinct',
        2 : 'Timeline timestamps are not decreasing',
        3 : 'Timeline timestamps are strictly increasing',
    }

    # Don't count more than these number of models
    aleph_nought = 1024



    @staticmethod
    def configure(key, value):

        if key == 'bot_count':
            assert value > 0
            Configuration.bot_count = value
            Configuration.thing_count = Configuration.bot_count + Configuration.obs_count
            return True

        if key == 'obstacle_count':
            assert value >= 0
            Configuration.obs_count = value
            Configuration.thing_count = Configuration.bot_count + Configuration.obs_count
            return True

        if key == 'stage_count':
            assert value >= 0
            Configuration.stage_count = value
            return True


        if key == 'x_dimension':
            assert value > 0
            Configuration.grid_dimension[0] = value
            Configuration.pt2_count = Configuration.grid_dimension[0] * Configuration.grid_dimension[1]
            return True

        if key == 'y_dimension':
            assert value > 0
            Configuration.grid_dimension[1] = value
            Configuration.pt2_count = Configuration.grid_dimension[0] * Configuration.grid_dimension[1]
            return True

        if key == 'timeline_interpretation':
            assert 0 <= value <= 3
            Configuration.timeline_interpretation = value
            return True

        if key == 'aleph_nought':
            assert value > 0
            Configuration.aleph_nought = value
            return True


        sys.stderr.write('Unknown configuration key: {0}\n'.format(key))
        return False

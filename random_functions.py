import random

def random_x() -> float:
    return random.uniform(0.3, 0.6)

def random_y() -> float:
    return random.uniform(0.7, 0.85)

def random_swipe_long(min_swipe_long, max_swipe_long) -> float:
    return random.uniform(min_swipe_long, max_swipe_long)

def random_swipe_time(min_swipe_time, max_swipe_time) -> float:
    return random.uniform(min_swipe_time, max_swipe_time)

def random_sleep_time(min_sleep_time, max_sleep_time) -> float:
    return random.uniform(min_sleep_time, max_sleep_time)

def random_pause(pause_probability) -> bool:
    num = random.randint(1,pause_probability)
    if num == 1:
        return True
    else:
        return False
    
def random_like(like_probability) -> bool:
    num = random.randint(1,like_probability)
    if num == 1:
        return True
    else:
        return False
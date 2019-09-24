def left_join(str) -> str:
    return ','.join(str).replace('right', 'left')

if __name__ == '__main__':
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"

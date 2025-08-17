import numpy as np
from numpy.typing import NDArray

def in_bounds(pos: NDArray[np.int_], shape: tuple[int, int]) -> bool:
    r, c = int(pos[0]), int(pos[1])
    return 0 <= r < shape[0] and 0 <= c < shape[1]

def move(
    robot_pos: NDArray[np.int_],
    direction: NDArray[np.int_],
    warehouse_map: NDArray[np.str_],
) -> NDArray[np.int_]:
    target = robot_pos + direction

    # 1) If target is out of bounds, no move
    if not in_bounds(target, warehouse_map.shape):
        return robot_pos

    cell = warehouse_map[target[0], target[1]]

    # 2) Wall blocks
    if cell == "#":
        return robot_pos

    # 3) Empty cell: move robot
    if cell == ".":
        # update map (optional if you’re keeping map authoritative)
        r0, c0 = robot_pos
        r1, c1 = target
        warehouse_map[r0, c0] = "."
        warehouse_map[r1, c1] = "@"
        return target

    # 4) Box: try to push
    if cell == "O":
        pushed_pos = check_valid_move(target, direction, warehouse_map)
        if pushed_pos is None:
            # chain blocked, robot stays
            return robot_pos

        # If push succeeded, move robot into 'target'
        r0, c0 = robot_pos
        r1, c1 = target
        warehouse_map[r0, c0] = "."
        warehouse_map[r1, c1] = "@"
        return target

    # Unexpected tile — treat as blocked
    return robot_pos


def check_valid_move(
    first_box_pos: NDArray[np.int_],
    direction: NDArray[np.int_],
    warehouse_map: NDArray[np.str_],
) -> NDArray[np.int_] | None:
    """
    Try to push a chain of boxes starting at first_box_pos one step in `direction`.
    Returns the position of the last box after the push if successful, else None.
    SIDE EFFECT: mutates warehouse_map when successful.
    """
    H, W = warehouse_map.shape
    moved_positions: list[NDArray[np.int_]] = []

    # Scan forward through the chain
    scan = first_box_pos.copy()

    # We know first_box_pos is in-bounds and currently 'O'
    while True:
        # Ensure scan is in-bounds before reading
        if not in_bounds(scan, (H, W)):
            return None  # fell off the map → cannot push

        tile = warehouse_map[scan[0], scan[1]]

        if tile == "O":
            moved_positions.append(scan.copy())
            scan = scan + direction  # step to look at the next cell
            continue

        # Stop at the first non-'O' tile
        if tile == "#":
            return None  # wall blocks the push

        if tile == ".":
            break  # we have space to push into

        # Any other char (e.g., '@') → treat as blocked
        return None

    # Now `scan` points at the **empty** cell right after the last box.
    # Push boxes from farthest to nearest so we don't overwrite.
    for pos in reversed(moved_positions):
        dst = pos + direction
        # Bounds already implied by the scan logic, but guard anyway:
        if not in_bounds(dst, (H, W)):
            return None
        warehouse_map[dst[0], dst[1]] = "O"

    # Clear the original position of the nearest box
    nearest = moved_positions[0]
    warehouse_map[nearest[0], nearest[1]] = "."

    # Return new position of the farthest box (optional/useful for debugging)
    return moved_positions[-1] + direction

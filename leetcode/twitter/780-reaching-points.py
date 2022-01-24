class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            elif ty > sy:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

            if sx == tx and sy == ty: return True
            if sx > tx or sy > ty: return False
        if sx == tx and sy == ty:
            return True
        else:
            return False



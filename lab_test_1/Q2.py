#!/usr/bin/env python3
"""Compact Rectangle examples: minimal, AI-doc, manual-doc.

Run: python rectangle_single.py [class_idx width height]
"""
class R:
    __slots__ = ("w","h")
    def __init__(self,w,h): self.w, self.h = w, h
    def area(self): return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

class RA:
    """AI: stores floats; area and perimeter methods."""
    __slots__ = ("w","h")
    def __init__(self,w,h): self.w,self.h = float(w),float(h)
    def area(self): return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

class RM:
    """Manual: dims as float; same API as RA."""
    __slots__ = ("w","h")
    def __init__(self,w,h): self.w,self.h = float(w),float(h)
    def area(self): return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

def compare_doc():
    a = (RA.__doc__ or "").strip()
    m = (RM.__doc__ or "").strip()
    mi = (R.__doc__ or "").strip()
    return {"auto": a, "manual": m, "minimal": mi,
            "auto_len": len(a), "manual_len": len(m), "minimal_len": len(mi)}

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 4:
        ch, w, h = sys.argv[1], sys.argv[2], sys.argv[3]
    else:
        ch = input("1=min 2=AI 3=manual [1]: ").strip() or "1"
        w = input("width: "); h = input("height: ")
    try:
        w = float(w); h = float(h)
    except Exception:
        print("numeric required"); sys.exit(1)
    cls = {"1": R, "2": RA, "3": RM}.get(ch, R)
    o = cls(w, h)
    print("Area:", o.area())
    print("Perimeter:", o.perimeter())
    c = compare_doc()
    print("\nDoc lengths (auto/manual/minimal):", c["auto_len"], c["manual_len"], c["minimal_len"])
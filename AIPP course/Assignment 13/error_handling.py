def read_file(f):
    try:
        return open(f).read()
    except FileNotFoundError:
        return f"❌ '{f}' not found"
    except Exception as e:
        return f"❌ {e}"

while (f := input("File: ").strip()) != "exit":
    r = read_file(f)
    print(r[:200] + "..." if len(r) > 200 and not r.startswith("❌") else r)
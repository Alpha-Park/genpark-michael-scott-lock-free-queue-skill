"""Example usage for Michael-Scott Queue Skill."""
from client import MichaelScottQueue

def main():
    print("Executing Michael-Scott Queue...")
    q = MichaelScottQueue()
    q.enqueue("MSG_DISPATCH_01")
    q.enqueue("MSG_DISPATCH_02")
    q.enqueue("MSG_DISPATCH_03")

    print(f"Enqueued 3 items, current length: {q.length}")
    m1 = q.dequeue()
    m2 = q.dequeue()
    print("Dequeued items:", m1, m2)
    assert m1 == "MSG_DISPATCH_01" and m2 == "MSG_DISPATCH_02"
    print("Michael-Scott Queue verified successfully!")

if __name__ == "__main__":
    main()

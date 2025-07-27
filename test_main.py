import subprocess

def test_output():
    print("\n🖨️ Running your program...\n")

    try:
        result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
        output = result.stdout.strip()
        output_lines = output.split('\n')
    except Exception as e:
        print("❌ Your code could not be run. Make sure there are no errors in main.py.")
        print(f"Error: {e}")
        return

    # 🔍 Show what was printed
    print("📄 Your program printed:")
    if output_lines == ['']:
        print("(nothing)")
    else:
        for i, line in enumerate(output_lines):
            print(f"{i+1}: {line}")
    print("")

    # 🔍 Searchable full output
    full_output = "\n".join(output_lines).lower()

    passed = 0
    total = 5

    # Check each message independently
    if any("hello, scotland!" in line.lower() for line in output_lines):
        print("✅ 'Hello, Scotland!' was printed.")
        passed += 1
    else:
        print("❌ 'Hello, Scotland!' is missing.")

    if "python" in full_output and "fun" in full_output:
        print("✅ Your message includes both 'Python' and 'fun'.")
        passed += 1
    else:
        print("❌ One line should include both 'Python' and 'fun'.")

    if "guido" in full_output and "rossum" in full_output:
        print("✅ You mentioned 'Guido van Rossum'.")
        passed += 1
    else:
        print("❌ One line should mention 'Guido van Rossum'.")

    if "odd" in full_output and "sock" in full_output:
        print("✅ You mentioned Odd Socks Day.")
        passed += 1
    else:
        print("❌ One line should mention 'Odd Socks Day'.")

    if "mistake" in full_output and "trying" in full_output:
        print("✅ You included the message about mistakes and trying.")
        passed += 1
    else:
        print("❌ One line should include both 'Mistakes' and 'trying'.")

    # Summary
    print(f"\n🎯 You got {passed} out of {total} correct.")

    if passed == total:
        print("🎉 All print statements passed! Fantastic work!")
    elif passed == 0:
        print("💡 Keep going — review your print statements and try again!")

if __name__ == "__main__":
    test_output()

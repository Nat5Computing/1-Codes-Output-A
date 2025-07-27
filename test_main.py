import subprocess

def test_output():
    print("\n🖨️ Running your program...\n")

    try:
        result = subprocess.run(["python3", "main.py"], capture_output=True, text=True, timeout=5)
        if result.returncode != 0:
            print("❌ Your program had an error and couldn't run properly.")
            print("🔧 Error message:\n" + result.stderr.strip())
            print("\n💡 Fix the error in your code before checking the print statements.")
            return
    except Exception as e:
        print("❌ Something went wrong when running your code.")
        print(f"Error: {e}")
        return

    output = result.stdout.strip()
    output_lines = output.split('\n')

    # Show actual output
    print("📄 Your program printed:")
    if not output.strip():
        print("(nothing)")
    else:
        for i, line in enumerate(output_lines):
            print(f"{i+1}: {line}")
    print("")

    # Now begin checking for expected content
    full_output = "\n".join(output_lines).lower()

    passed = 0
    total = 5

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

    print(f"\n🎯 You got {passed} out of {total} correct.")

    if passed == total:
        print("🎉 All print statements passed! Fantastic work!")
    elif passed == 0:
        print("💡 Keep going — review your print statements and try again!")

if __name__ == "__main__":
    test_output()

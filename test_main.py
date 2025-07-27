import subprocess

def test_output():
    try:
        result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
        output_lines = result.stdout.strip().split('\n')
    except Exception as e:
        print("❌ Your code could not be run. Make sure there are no errors in main.py.")
        print(f"Error: {e}")
        return

    passed = 0
    total = 5

    if len(output_lines) < 5:
        print(f"⚠️ Only {len(output_lines)} line(s) printed. 5 expected.")
        print("💡 Your program may have crashed before finishing.")
        print("🔍 Tip: Check for missing quotation marks, brackets, or other typos in your print statements.\n")

    full_output = "\n".join(output_lines).lower()

    # Check for Hello, Scotland!
    if any("hello, scotland!" in line.lower() for line in output_lines):
        print("✅ 'Hello, Scotland!' was printed.")
        passed += 1
    else:
        print("❌ 'Hello, Scotland!' is missing.")

    # Check for both 'python' and 'fun'
    if "python" in full_output and "fun" in full_output:
        print("✅ Your message includes both 'Python' and 'fun'.")
        passed += 1
    else:
        print("❌ One line should include both 'Python' and 'fun'.")

    # Check for Guido van Rossum
    if "guido" in full_output and "rossum" in full_output:
        print("✅ You mentioned 'Guido van Rossum'.")
        passed += 1
    else:
        print("❌ One line should mention 'Guido van Rossum'.")

    # Check for Odd Socks Day
    if "odd" in full_output and "sock" in full_output:
        print("✅ You mentioned Odd Socks Day.")
        passed += 1
    else:
        print("❌ One line should mention 'Odd Socks Day'.")

    # Check for Mistakes and Trying
    if "mistake" in full_output and "trying" in full_output:
        print("✅ You included the message about mistakes and trying.")
        passed += 1
    else:
        print("❌ One line should include both 'Mistakes' and 'trying'.")

    print(f"\n🎯 You got {passed} out of {total} lines correct.")

    if passed == total:
        print("🎉 All print statements passed! Fantastic work!")

if __name__ == "__main__":
    test_output()

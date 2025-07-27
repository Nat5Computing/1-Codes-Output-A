import subprocess

def test_output():
    result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
    output_lines = result.stdout.strip().split('\n')

    # Store pass/fail results
    passed = 0
    total = 5

    if len(output_lines) < 5:
        print(f"⚠️ Only {len(output_lines)} line(s) printed. 5 expected.\n")

    # Line 1
    try:
        assert output_lines[0] == "Hello, Scotland!"
        print("✅ Line 1 is correct!")
        passed += 1
    except:
        print("❌ Line 1 is incorrect. Should be: 'Hello, Scotland!'")

    # Line 2
    try:
        line2 = output_lines[1].lower()
        assert "python" in line2 and "fun" in line2
        print("✅ Line 2 is correct!")
        passed += 1
    except:
        print("❌ Line 2 should mention both 'Python' and 'fun'.")

    # Line 3
    try:
        line3 = output_lines[2].lower()
        assert "guido" in line3 and "rossum" in line3
        print("✅ Line 3 is correct!")
        passed += 1
    except:
        print("❌ Line 3 should mention 'Guido van Rossum'.")

    # Line 4
    try:
        line4 = output_lines[3].lower()
        assert "odd" in line4 and "sock" in line4
        print("✅ Line 4 is correct!")
        passed += 1
    except:
        print("❌ Line 4 should mention 'Odd Socks Day'.")

    # Line 5
    try:
        line5 = output_lines[4].lower()
        assert "mistake" in line5 and "trying" in line5
        print("✅ Line 5 is correct!")
        passed += 1
    except:
        print("❌ Line 5 should mention 'Mistakes' and 'trying'.")

    print(f"\n🎯 You got {passed} out of {total} lines correct.")

    if passed == total:
        print("🎉 All print statements passed! Fantastic work!")

if __name__ == "__main__":
    test_output()

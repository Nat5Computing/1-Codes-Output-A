import subprocess

def test_output():
    result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
    output_lines = result.stdout.strip().split('\n')

    # Check that there are at least 5 lines
    assert len(output_lines) >= 5, f"Expected at least 5 lines of output, but got {len(output_lines)}."

    # Line 1: Exact match
    assert output_lines[0] == "Hello, Scotland!", "Line 1 is incorrect. Should be: 'Hello, Scotland!'"

    # Line 2: Look for both 'python' and 'fun', case-insensitive
    line2 = output_lines[1].lower()
    assert "python" in line2 and "fun" in line2, "Line 2 should mention both 'Python' and 'fun'."

    # Line 3: Look for 'Guido' and 'Rossum'
    line3 = output_lines[2].lower()
    assert "guido" in line3 and "rossum" in line3, "Line 3 should mention 'Guido van Rossum'."

    # Line 4: Must mention 'Odd Socks' (flexible phrasing)
    line4 = output_lines[3].lower()
    assert "odd" in line4 and "sock" in line4, "Line 4 should mention 'Odd Socks Day'."

    # Line 5: Must contain the key phrase (can allow slight variation)
    line5 = output_lines[4].lower()
    assert "mistake" in line5 and "trying" in line5, "Line 5 should mention 'Mistakes' and 'trying'."

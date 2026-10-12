import sys
from stats import average_by_city, read_valid, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    
    blank_lines = 0
    for line in lines:
        if line.strip() == "":
            blank_lines += 1
            
    valid_records = read_valid(lines)
    broken_lines = len(lines) - len(valid_records) - blank_lines
    
    best_city = warmest_city(valid_records)
    averages = average_by_city(valid_records)
    
    if best_city:
        max_temp = averages[best_city]
    else:
        max_temp = 0.0
        
    print(len(valid_records))
    print(broken_lines)
    print(f"{max_temp:.1f}")

if __name__ == "__main__":
    main()
"""
Job Applicant Scoring System with Bias Analysis
"""

from collections import defaultdict

def calculate_score(exp, edu, skills, cert):
    return exp * 10 + edu * 15 + skills * 20 + cert * 5

def analyze_bias(apps):
    print("\n" + "=" * 50)
    print("BIAS ANALYSIS")
    print("=" * 50)
    gender_stats = defaultdict(list)
    for app in apps:
        gender_stats[app['gender']].append(app['score'])
    
    print("\nGender Statistics:")
    for gender, scores in gender_stats.items():
        print(f"  {gender}: Avg = {sum(scores)/len(scores):.2f}, Count = {len(scores)}")
    
    male = gender_stats.get('Male', [])
    female = gender_stats.get('Female', [])
    if male and female:
        diff = abs(sum(male)/len(male) - sum(female)/len(female))
        print(f"\nGender Difference: {diff:.2f}")
        print("⚠️  Bias detected!" if diff > 10 else "✓ No significant bias.")
    
    print(f"\nTop 5 Scores:")
    for i, app in enumerate(sorted(apps, key=lambda x: x['score'], reverse=True)[:5], 1):
        print(f"  {i}. {app['gender']}: {app['score']}")

def main():
    print("APPLICANT SCORING SYSTEM")
    choice = input("Enter manually? (y/n, 'n' for sample): ").lower()
    
    apps = []
    if choice == 'y':
        print("\nEnter applicants (press Enter on Gender to finish):")
        i = 0
        while True:
            gender = input(f"\nApplicant {i+1} Gender: ").strip()
            if not gender:
                break
            try:
                exp = int(input("Experience: "))
                edu = int(input("Education: "))
                skills = int(input("Skills: "))
                cert = int(input("Certifications: "))
                apps.append({'gender': gender, 'score': calculate_score(exp, edu, skills, cert)})
                i += 1
            except ValueError:
                print("Invalid input. Skipping.")
    else:
        import random
        random.seed(42)
        for _ in range(10):
            apps.append({
                'gender': random.choice(['Male', 'Female', 'Other']),
                'score': calculate_score(random.randint(0, 10), random.randint(1, 5), random.randint(1, 10), random.randint(0, 5))
            })
        print(f"Generated {len(apps)} sample applicants")
    
    if apps:
        analyze_bias(apps)

if __name__ == "__main__":
    main()

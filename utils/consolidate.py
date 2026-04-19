import json
import csv
import os

def consolidate_data():
    base_dir = '/home/nirvana/Documents/Side Hustle/Antigravity_Claude/DataRadar'
    csv_file = os.path.join(base_dir, 'data', 'jobs_extracted.csv')
    salary_file = os.path.join(base_dir, 'data', 'salaries.json')
    master_file = os.path.join(base_dir, 'data', 'master_data.json')
    
    # Load salaries
    with open(salary_file, 'r') as f:
        salaries = json.load(f)
    
    # Load jobs
    jobs = []
    if os.path.exists(csv_file):
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                company = row['Company']
                # Search for specific salary for this title if possible, else general
                salary_info = salaries.get(company, {})
                
                # Match title prefix or keywords
                title = row['Title']
                match = "General"
                for key in salary_info.keys():
                    if key in title:
                        match = key
                        break
                
                row['SalaryRange'] = salary_info.get(match, salary_info.get('General', 'Contact for details'))
                row['Gossips'] = salary_info.get('Gossips', 'No community data yet.')
                row['Sources'] = salary_info.get('Sources', [])
                
                # Add more detailed mock data for UI variety
                if "Developer" in title or "Engineer" in title:
                    row['Description'] = f"Join our elite engineering team at {company}. You will be responsible for building scalable, high-performance systems and contributing to our core architecture. We value clean code and innovative thinking."
                    row['Requirements'] = ["React/Node.js or Python", "System Design expertise", "CI/CD & DevOps knowledge", "Agile methodologies"]
                elif "Analyst" in title or "Data" in title:
                    row['Description'] = f"Work with large datasets to drive business decisions at {company}. You'll build dashboards, perform statistical analysis, and help define our data strategy."
                    row['Requirements'] = ["SQL & Python", "Data Visualization (Tableau/PowerBI)", "Statistical Modeling", "Business Intelligence"]
                else:
                    row['Description'] = f"As a {title} at {company}, you will play a key role in our growth. We are looking for a proactive professional with a passion for excellence and customer satisfaction."
                    row['Requirements'] = ["Relevant industry experience", "Stakeholder management", "Analytical mindset", "Project coordination"]

                jobs.append(row)
    
    # Save master data
    with open(master_file, 'w') as f:
        json.dump(jobs, f, indent=2)
    print(f"Master data updated: {len(jobs)} jobs.")

if __name__ == "__main__":
    consolidate_data()

import csv
import re
import os

def parse_markdown_to_stories(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    stories = []
    
    # Split by Epics
    epics = re.split(r'## Epic (\d+): (.+)', content)
    
    # Skip preamble
    if len(epics) < 2:
        return stories

    # Processing Epics (triads: preamble, number, title, content)
    # The split creates: [preamble, '1', 'Scale Configuration', 'content...', '2', 'Core Tuner', 'content...']
    
    current_epic = ""
    
    for i in range(1, len(epics), 3):
        epic_num = epics[i]
        epic_title = epics[i+1].strip()
        epic_content = epics[i+2]
        
        full_epic_name = f"Epic {epic_num}: {epic_title}"
        
        # Parse stories in this epic
        story_blocks = re.split(r'### US-(\d+\.\d+): (.+)', epic_content)
        
        # [preamble, '1.1', 'Title', 'content', '1.2', 'Title', 'content'...]
        for j in range(1, len(story_blocks), 3):
            story_id = f"US-{story_blocks[j]}"
            story_title = story_blocks[j+1].strip()
            # Clean content: remove surrounding newlines
            raw_content = story_blocks[j+2].strip()
            
            # Extract description vs acceptance criteria
            parts = strip_markdown_parts(raw_content)
            
            stories.append({
                'Summary': f"{story_id}: {story_title}",
                'Description': parts['description'],
                'Acceptance Criteria': parts['criteria'],
                'Epic': full_epic_name,
                'Issue Type': 'Story'
            })
            
    return stories

def strip_markdown_parts(text):
    # Split into Description text and Acceptance Criteria table
    # Simple heuristic: AC starts with "#### Acceptance Criteria"
    parts = text.split('#### Acceptance Criteria')
    
    desc = parts[0].strip()
    
    # Clean up formatting for CSV (Jira doesn't always like complex markdown, but basic is fine)
    # Convert single newlines to spaces in sentences, but keep paragraphs? 
    # Actually, keep strictly as is but remove excessive whitespace.
    
    ac = ""
    if len(parts) > 1:
        # It's a table. Let's keep the table markdown or convert to bullet points.
        # Jira supports markdown tables usually.
        ac = "#### Acceptance Criteria\n" + parts[1].strip()
    
    # Combine for main description field if we only have one field target
    # But usually creating a separate 'Acceptance Criteria' if the user has custom fields is hard without mapping.
    # We will put EVERYTHING in Description for safety.
    
    full_desc = f"{desc}\n\n{ac}"
    
    return {
        'description': full_desc,
        'criteria': ac
    }

def write_csv(stories, output_path):
    # Columns standard for Jira
    # Epic Link is tricky in CSV import for Next-Gen.
    # We will use "Labels" to tag the Epic, which allows easy filtering/linking later.
    fieldnames = ['Summary', 'Description', 'Issue Type', 'Labels']
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for story in stories:
            writer.writerow({
                'Summary': story['Summary'],
                'Description': story['Description'],
                'Issue Type': story['Issue Type'],
                'Labels': story['Epic'].replace(' ', '_').replace(':', '') # Basic label sanitization
            })

if __name__ == '__main__':
    md_path = r'f:\Development\SwarTuner\SwarTuner\documents\USER_STORIES.md'
    csv_path = r'f:\Development\SwarTuner\SwarTuner\documents\jira_import.csv'
    
    if os.path.exists(md_path):
        stories = parse_markdown_to_stories(md_path)
        write_csv(stories, csv_path)
        print(f"Successfully created {csv_path} with {len(stories)} stories.")
    else:
        print(f"File not found: {md_path}")

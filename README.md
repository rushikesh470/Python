# Alumni Tracking System

## Project created by:
**Ghotekar Rushikesh Babasaheb**  
Student of Amrutvahini College of Engineering, T.E. Computer Engineering Department (under Zensar Python and SQL Training)

## Project Overview
The **Alumni Tracking System** is a comprehensive database solution designed to manage alumni records, track their contributions, monitor event participation, and maintain an audit trail of changes. This system is essential for educational institutions or organizations that wish to engage with their alumni community by recording their donations, mentorship efforts, job placements, and participation in events.

### Main Features of the System
- **Alumni Records**: Store and manage alumni personal information, academic background, current employment status, and company details.
- **Contributions Tracking**: Record alumni contributions such as donations, mentorship programs, or job placements.
- **Event Management**: Manage alumni event participation, including types of participation (e.g., speaker, attendee, sponsor) and feedback.
- **Change Logs**: Maintain logs for any updates made to alumni records to ensure accountability and transparency.
- **Reports**: Generate reports on alumni contributions, event participation, and summary statistics for better decision-making.

## Database Schema

### 1. Alumni Table
This table stores basic information about each alumni, including their personal details, graduation year, major, and current professional role.

**Key Fields:**
- **alumni_id**: Unique identifier for each alumni (Primary Key).
- **first_name**: Alumni's first name.
- **last_name**: Alumni's last name.
- **email**: Contact email address.
- **graduation_year**: Year of graduation.
- **major**: Academic field of study.
- **current_position**: Current job title or position.
- **company_name**: Name of the organization where the alumni is currently employed.

### 2. Contributions Table
This table records the various types of contributions made by alumni, such as donations, job placements, and mentorship activities.

**Key Fields:**
- **contribution_id**: Unique identifier for each contribution (Primary Key).
- **alumni_id**: The alumni who made the contribution (Foreign Key referencing the Alumni table).
- **description**: Detailed description of the contribution.
- **contribution_date**: Date when the contribution was made.
- **contribution_type**: Type of contribution (e.g., Donation, Mentorship, Job Placement).
- **amount**: Amount donated if the contribution is monetary.
- **achievement**: Description of the achievement resulting from the contribution (e.g., funding for a scholarship).

### 3. Events Table
This table stores information about alumni events such as networking events, reunions, and career development workshops.

**Key Fields:**
- **event_id**: Unique identifier for each event (Primary Key).
- **event_name**: Name of the event.
- **event_date**: Date the event took place.
- **event_location**: The venue where the event was held.
- **event_description**: A brief description of the event and its objectives.

### 4. Event Management Table
This table tracks alumni participation in events. It includes information about their type of involvement (speaker, attendee, sponsor) and feedback provided after the event.

**Key Fields:**
- **event_management_id**: Unique identifier for each event participation record (Primary Key).
- **alumni_id**: The alumni who participated in the event (Foreign Key referencing the Alumni table).
- **event_id**: The event the alumni participated in (Foreign Key referencing the Events table).
- **participation_type**: Type of participation (e.g., Speaker, Attendee, Sponsor).
- **feedback**: Feedback or comments provided by the alumni regarding the event.

### 5. Logs Table
This table captures any updates, inserts, or deletes made to alumni records for auditing and tracking changes over time.

**Key Fields:**
- **log_id**: Unique identifier for each log entry (Primary Key).
- **action**: The type of action performed (e.g., 'INSERT', 'UPDATE', 'DELETE').
- **action_date**: The date and time when the action occurred.
- **table_name**: Name of the table affected by the action.
- **old_value**: The value before the action (used for updates).
- **new_value**: The value after the action (used for updates).

## Key Features and Functionalities

### Alumni Information Management
The system allows users to store and manage detailed alumni profiles, including their contact details, academic background, and current professional status. This data is essential for maintaining an up-to-date alumni database.

### Contribution Tracking
The Contributions table allows you to track various contributions made by alumni, whether financial (e.g., donations) or non-financial (e.g., mentorship). The data helps in understanding the ways in which alumni are contributing to the institution or community.

### Event Participation
The system allows you to monitor alumni participation in events. Whether an alumni is a speaker, sponsor, or attendee, this system captures their involvement and feedback, which can be useful for future event planning.

### Audit and Change Tracking
The **Logs Table** provides an audit trail of all changes made to alumni records. Every insert, update, or delete action is recorded to ensure that any changes to alumni data can be reviewed or reversed if necessary. This is crucial for maintaining data integrity and accountability.

### Reports and Analytics
The system includes several predefined queries to generate reports:
- **Alumni Contributions Report**: A list of alumni and the contributions they've made, including the type and amount.
- **Total Contribution by Alumni**: A report that calculates the total amount of donations made by each alumni.
  
These reports can assist in understanding trends in alumni engagement, allowing organizations to plan future initiatives and strengthen alumni relations.

## Triggers for Data Integrity
The system includes triggers to ensure data consistency and integrity. For example, when alumni information is updated, the system automatically logs these changes into the **Logs Table**. This helps maintain a transparent record of all modifications.

**Example Trigger:**
- **Trigger for Alumni Updates**: A trigger that logs any updates made to the alumni's name or email into the `Logs` table.

### Procedure for Event Management
The system includes a stored procedure, `manage_event_participation`, which is used to handle event registrations and participation of alumni. The procedure automatically generates event participation records using a sequence for unique IDs.

**Procedure Functionality:**
- Inserts a new record into the **Event_Management** table when an alumni participates in an event.
- Captures feedback from alumni regarding their event experience.

## Setup Instructions

### Database Setup
1. **Create Tables**: Use the provided SQL scripts to create the tables (`Alumni`, `Contributions`, `Events`, `Event_Management`, `Logs`) in your database.
2. **Insert Sample Data**: Populate the tables with sample data using the `INSERT INTO` statements provided.
3. **Create Sequence**: Ensure that the sequence `Event_Management_SEQ` is created to generate unique IDs for the `Event_Management` table.
4. **Create Triggers**: Set up triggers to automatically log changes made to alumni records (e.g., when an alumni's information is updated).
5. **Create Procedures**: Create stored procedures such as `manage_event_participation` to handle event registration and alumni feedback.

### Running Reports
The system includes several queries for generating reports on alumni contributions, event participation, and total donations. These reports can be executed directly from the SQL interface of your database management tool.

## Prerequisites
- Python 3.x
- MySQL
- Flask

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/alumni-tracking-system.git
cd alumni-tracking-system

### 2. Install Dependencies
bash
pip install Flask mysql-connector-python
###3. Database Configuration
Create a MySQL database named alumni_tracking_system.

Configure the database connection in the code with your MySQL credentials.

python
db_config = {
    'host': 'localhost',
    'user': 'your_mysql_username',
    'password': 'your_mysql_password',
    'database': 'alumni_tracking_system'
}
Usage
Running the Application
Start the Flask Application

bash
python app.py
Access the Application

Open your web browser and navigate to http://localhost:5000

API Endpoints
Get All Alumni
URL: /alumni

Method: GET

Description: Retrieve all alumni records.

Add New Alumni
URL: /alumni

Method: POST

Description: Add a new alumni record.

Request Body:

json
{
    "name": "John Doe",
    "graduation_year": 2020,
    "degree": "B.Tech",
    "current_position": "Software Engineer",
    "contact_info": "john.doe@example.com"
}
Get Specific Alumni Details
URL: /alumni/<int:id>

Method: GET

Description: Retrieve details of a specific alumni using their ID.

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

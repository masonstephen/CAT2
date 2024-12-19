# Event Management System

## Group Members
- Member 1: 113832
- Member 2: 100485
- Member 3: 148285
- Member 4: 148327
- Member 5: 89229
- Member 6: 95306

## Project Implementation

### Models and Relationships
1. **Event**
   - Fields: title, description, date, organizer (ForeignKey), venue (ForeignKey)
   - Relationships: Each event belongs to an organizer and a venue

2. **Organizer**
   - Fields: user (OneToOneField)
   - Relationships: Each organizer is a user

3. **Venue**
   - Fields: name, location
   - Relationships: None

4. **Ticket**
   - Fields: event (ForeignKey), attendee (ForeignKey), status
   - Relationships: Each ticket belongs to an event and an attendee

5. **Attendee**
   - Fields: user (OneToOneField)
   - Relationships: Each attendee is a user

### Views/Viewsets and Roles
- **EventViewSet**: Handles CRUD operations for events.
- **OrganizerViewSet**: Handles CRUD operations for organizers.
- **VenueViewSet**: Handles CRUD operations for venues.
- **TicketViewSet**: Handles CRUD operations for tickets.
- **AttendeeViewSet**: Handles CRUD operations for attendees.

### Serializers
- **EventSerializer**: Validates event data and converts between JSON and Python objects.
- **OrganizerSerializer**: Validates organizer data and converts between JSON and Python objects.
- **VenueSerializer**: Validates venue data and converts between JSON and Python objects.
- **TicketSerializer**: Validates ticket data and converts between JSON and Python objects.
- **AttendeeSerializer**: Validates attendee data and converts between JSON and Python objects.

### URL Patterns
- `/api/events/`: Lists all events, allows creating a new event.
- `/api/events/<id>/`: Retrieves, updates, or deletes a specific event.
- `/api/organizers/`: Lists all organizers, allows creating a new organizer.
- `/api/venues/`: Lists all venues, allows creating a new venue.
- `/api/tickets/`: Lists all tickets, allows creating a new ticket.
- `/api/attendees/`: Lists all attendees, allows creating a new attendee.

### Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/masonstephen/Stephen-Mason-113832.git
    cd Stephen-Mason-113832
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```
	for this project credential for testing is this(if you don't want to create a superuser):
	admin/organizer: User name = Admin password =admin1234
	attendee: User name = User password = user1234 

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open a web browser and go to `http://127.0.0.1:8000`

### Testing
- **Test Cases**: Tested all CRUD operations for each model.
- **Test Methods**: Used Django REST framework's APIClient for testing endpoints.
- **Results**: All tests passed successfully.

### How to Run Tests
1. Ensure you have Django and Django REST framework installed.
2. Navigate to your project directory.
3. Run tests using:

    ```bash
    python manage.py test
    ```

### Manual Testing with Postman
1. Import the Postman collection provided.
2. Test each endpoint manually.
3. Ensure that all HTTP methods (GET, POST, PUT, DELETE) work as expected.
4. Document any issues and resolve them.


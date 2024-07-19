# Email Guesser Application

This application is created as home assingment for babbel. It includes frontend and backend services to 
guess possible email address of the contact for babbel using fullname and domain address.

## Requirements

Docker with compose plugin is enough to run this application.

## Usage

1. Start services by: ``docker compose up --build -d``
2. Run fixture loading script by: ``docker compose exec backend python scripts/load_fixture.py``
3. Go to ``http://localhost:3000`` to interact with frontend.


## Testing

### Backend

Run ``docker compose exec backend make test``

### Frontend

Run ``docker compose exec frontend yarn test:coverage``

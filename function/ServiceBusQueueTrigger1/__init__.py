import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def main(msg: func.ServiceBusMessage):

    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info(
        'Python ServiceBus queue trigger processed message: %s', notification_id)

    # DONE: Get connection to database
    # establishing the connection
    conn = psycopg2.connect(
        database="techconfdb",
        user='femmyte@femmyte-server',
        password='Library@1234',
        host='femmyte-server.postgres.database.azure.com',
    )

    # Setting auto commit false
    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    logging.info('Retrieved database connection successfully...')

    try:
        # TODO: Get notification message and subject from database using the notification_id
        logging.info(
            'Quering PostgresSQL database for notification message and subject using the notification_id')
        notification_query = """SELECT message, subject from notification where id = %s"""
        cursor.execute(notification_query, (int(notification_id)))
        notification = cursor.fetchone()
        logging.info('Printing notification output...', notification)
        print("Connection established to: ", notification)

        # TODO: Get attendees email and name
        # Fetching 1st row from the table
        attendees_query = '''SELECT email, CONCAT(first_name, last_name) AS name from attendee'''
        cursor.execute(attendees_query)
        attendees = cursor.fetchall()
        count = cursor.rowcount
        print("Connection established to: ", attendees)
        logging.info('fetching attendees email and name')
        # TODO: Loop through each attendee and send an email with a personalized subject
        if attendees:
            for attendee in attendees:
                logging.info(
                    "Looping through each attendee to send an email with a personalized subject")
                message = Mail(
                    from_email='sanyaoluadefemi@gmail.com',
                    to_emails=attendee.email,
                    subject=notification.subject,
                    html_content=f'<strong>{notification.message}</strong>')

                try:
                    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                    response = sg.send(message)
                    print(response.status_code)
                    print(response.body)
                    print(response.headers)
                except Exception as e:
                    print(e.message)
        # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        notification_update_query = """Update notification set completed_date = %s, status =%s  where id = %s"""
        cursor.execute(notification_update_query, (datetime.utcnow(),
                       f'Notified {count} Attendees', int(notification_id)))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        # TODO: Close connection
        if conn:
            cursor.close()
            conn.close()

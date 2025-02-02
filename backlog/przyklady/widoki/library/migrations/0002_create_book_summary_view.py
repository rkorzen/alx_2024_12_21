# Generated by Django 5.1.4 on 2025-01-31 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
                migrations.RunSQL(
            """
            CREATE VIEW book_summary AS
            SELECT library_book.id, library_book.title, library_author.name AS author_name, library_book.price
            FROM library_book
            JOIN library_author ON library_book.author_id = library_author.id;
            """,
            reverse_sql="DROP VIEW IF EXISTS book_summary;"
        ),
    ]

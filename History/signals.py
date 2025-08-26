from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tweet, History


@receiver(post_save, sender=Tweet)
def create_history_on_tweet_creation(sender, instance, created, **kwargs):
    """
    Django Signal to create a History entry when a new Tweet is saved.
    """
    if created:
        # Get the user from the instance of the Tweet model
        user = instance.user
        method = "POST"

        # Create the summary message using the user's username
        summary_message = f"User {user.username} created a tweet with content: '{instance.content}'"

        # Create and save the new History object
        History.objects.create(
            user=user,
            method=method,
            tweet=instance,
            summary=summary_message
        )
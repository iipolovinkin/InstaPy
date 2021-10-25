"""
This template is written by @Tachenz

What does this quickstart script aim to do?
- Interact with user followers, liking 3 pictures, doing 1-2 comment - and
25% chance of follow (ratios which work the best for my account)

NOTES:
- This is used in combination with putting a 40 sec sleep delay after every
like the script does. It runs 24/7 at rather slower speed, but without
problems (so far).
"""

from instapy import InstaPy
from instapy import smart_run

# get a session!
session = InstaPy(username='', password='')

photo_comments = ['Красиво :heart:',
    'Вы прекрасны :heart_eyes:',
    'Классно :thumbsup:',
    'Фото супер :fire:',
    'Атмосферно :fire:',
    'Невероятное фото :fire:',
    'Тут точно лайк :heart_eyes:',
    'Очень :heart_eyes:',
    'Как же красиво :heart:']

# let's go! :>
with smart_run(session):
    # settings
    session.set_user_interact(amount=2, randomize=True, percentage=100)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    min_followers=50,
                                    min_following=20)
        # max_followers=3000,
        # max_following=1500,
    session.set_simulation(enabled=False)
    session.set_do_like(enabled=True, percentage=100)
    session.set_ignore_users([])
    session.set_do_comment(enabled=True,  comment_liked_photo=True, percentage=100)
    # session.set_do_follow(enabled=True, percentage=50, times=1)
    session.set_comments(photo_comments)
    session.set_ignore_if_contains([])
    # session.set_action_delays(enabled=True, like=1)

    # activity
    # session.interact_user_followers(['malina_glina'], amount=340)
    progress_file: str = 'progress\\progress1.txt'
    session.interact_user_followers(['garderob_naya'], amount=200, exist_persons_file=progress_file)

    """ Joining Engagement Pods...
    """
    # session.join_pods(topic='entertainment', engagement_mode='no_comments')
"""
-- REVIEWS --

@Andercorp:
- This would probably be the best temp for new accounts to start slowly and 
gently and then as your account gather IG authority, you could put some more 
power to your temp/bot...

@uluQulu:
- @Tachenz, the values in your script took my attention, it will be very 
good for new starters, as @Andercorp said. Stunning!

"""

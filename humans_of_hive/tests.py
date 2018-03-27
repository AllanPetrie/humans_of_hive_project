from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders

class GeneralTests(TestCase):
    def test_serving_static_files(self):
        # If using static media properly result is not NONE once it finds hive.jpg
        result = finders.find('images/hive.jpg')
        self.assertIsNotNone(result)

class TemplateTests(TestCase):
    def test_home_using_template(self):
        # Check home page is rendered using template
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'humans_of_hive/home.html')

    def test_about_using_template(self):
        # Check about page is rendered using template
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'humans_of_hive/about.html')

    def test_hall_of_fame_using_template(self):
        # Check hall of fame page is rendered using template
        response = self.client.get(reverse('hall_of_fame'))
        self.assertTemplateUsed(response, 'humans_of_hive/hall_of_fame.html')

    def test_register_using_template(self):
        # Check registration page is rendered using template
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'humans_of_hive/register.html')

    def test_login_using_template(self):
        # Check login page is rendered using template
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'humans_of_hive/login.html')

    def test_view_profile_using_template(self):
        # Check post page is rendered using template
        response = self.client.get(reverse('show_post'))
        self.assertTemplateUsed(response, 'humans_of_hive/view_post.html')

    def test_user_profile_using_template(self):
        # Check profile page is rendered using template
        response = self.client.get(reverse('user_profile'))
        self.assertTemplateUsed(response, 'humans_of_hive/user_profile.html')

    def test_add_post_using_template(self):
        # Check post adding page is rendered using template
        response = self.client.get(reverse('add_post'))
        self.assertTemplateUsed(response, 'humans_of_hive/add_post.html')

    def test_add_comment_using_template(self):
        # Check comment adding page is rendered using template
        response = self.client.get(reverse('add_comment'))
        self.assertTemplateUsed(response, 'humans_of_hive/add_comment.html')

    def test_user_posts_using_template(self):
        # Check page displaying user posts is rendered using template
        response = self.client.get(reverse('user_posts'))
        self.assertTemplateUsed(response, 'humans_of_hive/user_posts.html')

    def test_add_follower_using_template(self):
        # Check follower adding page is rendered using template
        response = self.client.get(reverse('add_follower'))
        self.assertTemplateUsed(response, 'humans_of_hive/add_follower.html')

    def test_remove_follower_using_template(self):
        # Check follower removing page is rendered using template
        response = self.client.get(reverse('remove_follower'))
        self.assertTemplateUsed(response, 'humans_of_hive/remove_follower.html')

class AboutPageTests(TestCase):
    def test_about_contains_creator_message(self):
        # Check about page contains message
        response = self.client.get(reverse('about'))
        self.assertIn(b'Humans of Hive was created by:', response.content)

    def test_about_contains_image(self):
        # Check about page for image
        response = self.client.get(reverse('about'))
        self.assertIn(b'img src="/static/images/hive.jpg', response.content)

class ViewsTests(TestCase):
    def test_admin_interface_page_view(self):
        # check admin interface - is it configured and set up
        from admin import PageAdmin
        self.assertIn('category', PageAdmin.list_display)
        self.assertIn('url', PageAdmin.list_display)

class ModelsTests(TestCase):
    def set_up(self):
        #Check if population script runs
        try:
            from populate_humans_of_hive import populate
            populate()
        except ImportError:
            print('The module populate_humans_of_hive does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function')

    def test_post_slug_field_work(self):
        #Test the slug field works
        from humans_of_hive.models import Post
        post = Post(title='new post slug')
        post.save()
        self.assertEqual(post.slug, 'new-post-slug')

class FormsTests(TestCase):
    def set_up(self):
        #Check that forms exists
        try:
            from forms import PostForm
            from forms import CommentForm
            from forms import UserForm
            from forms import UserProfileForm
        except ImportError:
            print('The module forms does not exist')
        except NameError:
            print('Some form does not exist or is not correct')
        except:
            print('Something else went wrong :-(')
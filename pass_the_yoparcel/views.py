import random
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import MagicWord, Person
from .forms import WordForm


def index_view(request):

    if request.method == 'POST':
        # The request is a post!
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word'].strip().lower()
            if word.isalpha():
                # If anything is funky, just fall back to the GET behaviour
                return HttpResponseRedirect(word)

    # Get all 'used' recipients in order (mapped to a MagicWord)
    recipients = map(lambda a: a.recipient,
                     MagicWord.objects.exclude(recipient=None).select_related('recipient').order_by('index'))
    context = {
        'recipients': recipients
    }
    return render(request, 'pass_the_yoparcel/index.html', context)


def word_view(request, word):
    try:
        # Get the MagicWord object.
        this_magic_word = MagicWord.objects.get(word=word)

        # If you're here, this_magic_word should have a recipient_id
        if this_magic_word.recipient is None:
            return render(request, 'pass_the_yoparcel/locked.html', status=400)

        # Try to get the next magic word, who's recipient we are about to choose
        try:
            next_index = this_magic_word.index + 1
            next_magic_word = MagicWord.objects.get(index=next_index)

            if next_magic_word.recipient is None:

                # Choose and set a recipient on next_magic_word
                all_person_ids = set(map(lambda p: p.id, Person.objects.all()))
                used_person_ids = set(filter(None, map(lambda r: r.recipient_id, MagicWord.objects.all())))

                candidates = list(all_person_ids.difference(used_person_ids))
                choice = random.choice(candidates)

                next_magic_word.recipient = Person.objects.get(id=choice)
                next_magic_word.save()

                context = {
                    'status': 'not_chosen',
                    'this_magic_word': this_magic_word,
                    'next_magic_word': next_magic_word
                }
                return render(request, 'pass_the_yoparcel/word.html', context)
            else:
                # You've already chosen a destination, let's print it out
                context = {
                    'status': 'chosen',
                    'this_magic_word': this_magic_word,
                    'next_magic_word': next_magic_word
                }
                return render(request, 'pass_the_yoparcel/word.html', context)

        except MagicWord.DoesNotExist:
            # We're at the end of the chain!
            context = {
                'status': 'end',
                'this_magic_word': this_magic_word
            }
            return render(request, 'pass_the_yoparcel/word.html', context)

    except MagicWord.DoesNotExist:
        # You entered a word that doesn't exist!
        return render(request, 'pass_the_yoparcel/not_found.html', status=404)

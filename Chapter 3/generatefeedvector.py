import feedparser
import re


# Returns title and dictionary of word counts for an RSS feed
def get_word_counts(url):
    # Parse the feed
    d = feedparser.parse(url)
    wc = {}

    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e: summary = e.summary
        else: summary = e.description

        # Extract a list of words
        words = get_words(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1

        return d.feed.title, wc


def get_words(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split the words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


apcount = {}
word_counts = {}
feed_list = [line for line in file('feedlist.txt')]
for feed_url in feed_list:
    try:
        (title, wc) = get_word_counts(feed_url)
        word_counts[title] = wc
        for (word, count) in wc.items():
            apcount.setdefault(word, 0)
            if count > 1:
                apcount[word] += 1
    except:
        print 'Failed to parse feed %s' % feed_url

word_list = []
for (w, bc) in apcount.items():
    frac = float(bc) / len(feed_list)
    if 0.1 < frac < 0.5:
        word_list.append(w)

out = file('blogdata.txt', 'w')
out.write('Blog')
for word in word_list:
    out.write('\t%s' % word)
out.write('\n')
for (blog, wc) in word_counts.items():
    print blog
    out.write(blog)
    for word in word_list:
        if word in wc:
            out.write('\t%d' % wc[word])
        else:
            out.write('\t0')
    out.write('\n')
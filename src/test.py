hey = """Norah Jones's NYC Residency Reveals the Best Contradictions of Her Career
https://www.pastemagazine.com/articles/2017/09/norah-jones-nyc-residency-reveals-the-best-contrad.html
Carly Simon and the Mystery of "You're So Vain"
https://www.pastemagazine.com/articles/2017/10/from-the-vault-the-mystery-of-carly-simons-youre-s.html
The 10 Biggest Broadway Turns By Rock Stars
https://www.pastemagazine.com/articles/2017/10/the-10-biggest-broadway-appearances-by-rock-stars.html
Roberta Flack, Lauryn Hill and the Legacy of "Killing Me Softly With His Song"
https://www.pastemagazine.com/articles/2017/09/exclusive-roberta-flack-lauryn-hill-and-the-legacy.html""".split('\n')


hey = """Them Are Us Too and the Fabric of Grief
https://www.popmatters.com/them-are-us-too-amends-2581919233.html
Cullen Omori Indulges Listeners with 'The Diet'
https://www.popmatters.com/cullen-omori-the-diet-review-2596198800.html
Madeline Kenney: Night Night at the First Landing
https://www.popmatters.com/madeline-kenney-night-night-at-the-first-landing-2495382193.html
Shopping Checks Out on Third Album ‘The Official Body’
https://www.popmatters.com/shopping-the-official-body-2525504243.html""".split('\n')


hey = """I’m Obsessed With My Ex’s New Girlfriend
https://humanparts.medium.com/im-obsessed-with-my-ex-s-new-girlfriend-855c91337ead
You Will
https://nailedmagazine.com/fiction/you-will-claire-greising/
Less-Than-Strange Window: A Hunt for the Supernatural at BAM
http://blog.bam.org/2018/10/less-than-strange-window-hunt-for.html
Another Story About The End Of The World
http://potluckmag.com/may-2016/2016/5/4/another-story-about-the-end-of-the-world""".split('\n')

import numpy as np
you = np.asarray(hey).reshape(int(len(hey)/2),2).tolist()

for item in you:
    new_string = ''.join(['* ', '[',item[0], ']','(', item[1], ')'])
    print(new_string)


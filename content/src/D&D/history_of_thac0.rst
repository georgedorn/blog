A history of hitting things in D&D
##################################

###########################
From Tables to THAC0 to DC.
###########################

:date: 2019-04-16
:tags: D&D, mechanics, history
:category: D&D
:slug: history_of_thac0

In working on the as-yet unnamed homebrew Basic [#basic]_ D&D derivative, I'm having to make some choices about what features from post-Basic editions I'd like to adopt.  In doing so, I was reminded of an argument at the game table about which edition invented THAC0 - was it 1st edition AD&D or 2nd?  The answer is far more complicated.

The Examples
------------

Along the way, I'll be using two example scenarios:

* a first-level fighter with a longsword, and just enough strength to gain a +1 to attack rolls (a 13 in many editions, a 12 in others), trying to hit a goblin
* a first-level archer (fighter where applicable) trying to hit a enemy with significant armor, such as a dragon. For this example, a +2 to-hit bonus is used; it could be a bonus from Dexterity (where applicable), race (halflings) or a +2 magical bow.

Brown Book D&D (1974)
---------------------
From the beginning, D&D relied on charts.  You used your level and the AC of the monster and tried to roll over the number to hit.  However, at this stage, AC ranged only from 9 (no armor) to 2 (Plate armor and shield) and level improvements to your target number occurred every 3 (fighters) to 5 (magic users) levels.  This resulted in a very small chart.

There are several other oddities, at least to our modern sensibilities, but only worth mentioning briefly:

* the only bonus/penalty to hit was for missile attacks from high/low Dexterity characters.
* Monsters fighting "normal men" rolled an attack for every Hit Die; the +X part was a bonus given to one of those attacks.
* the party was expected to consist of about 20 PCs; this makes the "number appearing" column of the monster chart make more sense - you typically encountered 40-400 goblins!

Our examples are both rudimentary and straightforward: the fighter needs to roll a 13 to hit a goblin (no strength bonus existed), the archer needs a 15 to hit a dragon (given +1 from dexterity and +1 from a magical bow).


Basic (1977 - 1983+)  [#basic]_
-------------------------------
Red Book Basic (TSR2014) had an extremely simple Hit Roll Table:

.. image:: images/1974_red_book_to_hit.jpg

Because the book only went to third level, all player characters had the same target roll.  Our fighter needs to roll a 12 on the 20-sided die (and then add 1 to it for 13) to hit the goblin (AC 6).

Our archer example however, reveals the first interesting wart of the chart system: the cap of 20.  A roll of 20 was the most that could be required to hit anything at the time, and most importantly this is not a natural 20 but one after bonuses.  Our low-level archer can hit both a Red dragon (AC -1) or a Gold dragon (AC -2) on a total to-hit roll of 20, which means a natural roll of 18 or better.

This wart significantly benefits characters with bonuses to hit, whether magical or otherwise.  Further books, from Companion to Rules Cyclopedia, standardized the table to repeat the 20 exactly five times before moving on to 21.  The full chart, after expansion by subsequent books (from the DM's Screen, TSR9431):

.. image:: images/basic_complete_to_hit.jpg

So our archer example goes even further, also hitting the "large" versions of our Red (AC -3) and Gold (AC -4) dragons, and even up to a "huge" Red dragon (AC -5), all on a natural roll of 18 or better.  It's not until he tangles with a huge Gold dragon (AC -6) that the difficulty increases again (needing a natural 19).

It's also worth noting that Basic had no concept of a critical hit.  A natural 20 was not a guaranteed hit; our archer can do amazing things due to the +2 to hit, but has zero chance of hitting a monster with AC -8.

Two more oddities appeared over the years.  After the 20-plateau, the chart increases steadily to 30, where we have another plateau for 5 ACs.  And higher-level characters trying to hit poorly-armored targets find the to-hit number dropping to zero, and then they start getting extra damage added to every hit; a 36th-level fighter only misses a goblin on natural 1 (the first mention of this) and does an extra 5 points of damage.

AD&D First Edition (1979)
-------------------------

1e buried the to-hit chart in the DMG.  Here's the fighter chart:

.. image:: images/first_edition_to_hit_fighters.jpg

A bit counter-intuitive to read, so our fighter example can illustrate.  To hit a goblin (still AC 6), our fighter needs a natural roll of 13 (to which +1 is added for a total of 14).

Our archer example reveals that not only has Basic's 20-plateau persisted, it stretched to 6 entries instead of 5!  Now our archer can hit anything from a 0 to -5 AC on a natural 18 or better.  At the same time, many monsters have seen their armor nerfed; of the dragons, only a Chromatic (AC 0), Red or Silver (AC -1), Gold (AC -2) or Platinum (AC -3) fall in this range.  To see an AC -5 we have to look into the ranks of demons and devils.

Curiously, in Appendix E of the DMG, we have our first mention of a single figure meant to simplify the chart: a column called "To Hit A.C. 0".

.. image:: images/first_edition_to_hit_zero.jpg

Despite the name, this isn't a proper THAC0 as it was later known; there are no explanations of how to use this number, except presumably to compare monsters and perhaps make it easier to look up the right column in the monster to-hit matrix.  The Monster Manual does not print the number at all.

AD&D Second Edition (1989)
--------------------------
2e brought about the first *core* rulebook to mention the THAC0 mechanic.  The 1996 printing puts it simply:

  **Figuring the To-Hit Number**
  The first step in making an attack roll is to find the number needed to hit the target.  Subtract the Armor Class of the target from the attacker's THAC0 (Remember that if the Armor Class is a negative number, you *add* it to the attacker's THAC0.)  The character has to roll the resulting number, or higher, on 1d20 to hit the target.
  
THAC0 officially removed the 20-plateau wart, for better or worse, and also made it easier to preemptively include your typical bonuses and penalties for any given weapon.  We could say that our fighter has a THAC0 of 20 and a +1 to hit, or we could just say he has a THAC0 of 19.  They're logically equivalent.  To hit that goblin (AC 6, still), the fighter needs a natural 13.

To compensate for the now-missing wiggle room at the edge of your character's abilities, for the first time we see rules stating that a 20 always hits.  This is a small consolation for the archer with the magic bow, however.  Where a natural 18 would hit a wide range of dragons, that 18 will only hit AC 0 targets now - Blue and Green dragons.  Coupled with a de-nerfing of monsters in 2e, a natural 20 is needed for almost every other well-known dragon type.

The natural 20 rule also has interesting side effects; without additional countermeasures, a small army of scrubs (goblins, kobolds, bullywugs) can outclass the most absurdly armored high-tier enemy, simply by arming themselves with ranged weapons and hoping for natural 20s.

When was THAC0 Invented?
------------------------

AD&D Second edition was the first *core* book to make use of THAC0.  However, several other books made use of it before development of 2e began in 1987.  The Basic line of books, for example, had a very inconsistent attitude towards its use:

* AC1, The Shady Dragon Inn, 1983, Carl Smith: includes THAC0 for pregenerated PCs, but only says what the acronym stands for, not the mechanics it implies.
* B10, Night's Dark Terror, 1986, UK: Includes THAC0 and how to use it, but says "in most cases, the roll needed to hit other armour classes = THAC0 *minus* AC," alluding to parts of the chart it cannot replicate.
* B11, King's Festival, 1989, Carl Sargent: includes THAC0 for monsters and NPCs, and explains the mechanics, suggesting that you use it and ditch the tables entirely.
* But even later, some adventure modules avoid using it, while earlier modules in the same series was happy to adopt it.  For example, CM7 (1986) makes use of it, but CM9 (1987) avoids it.

AD&D First Edition also included it in some publications, though with similarly fuzzy attitude for whether it augmented or replaced the tables:

* RPGA 1, To The Aid of Falx, Mentzer, 1982:  Might be the first use of the THAC0 acronym ever published, but how to use it is left as unexplained as in the 1e DMG.
* RPGA 3, The Forgotten King, 1983:  Uses THAC0 for monsters and NPCs, with a special notation, seemingly an attempt to encode the 20-plateau. |note|
* UK4, When A Star Falls, 1984: Similarly uses THAC0 and explains the mechanics with the a caveat as B10, as well as occasionally including a star in the notation to suggest looking up the chart in specific cases.

.. |note| image:: images/rpga3_thac0.jpg

I Have A Theory
_______________

I have a theory, then, that when the 1e DMG was published in 1979, the inclusion of the monster summary tables and the column called "To Hit A.C. 0" got groups of players thinking about how to simplify the mechanic. Perhaps within the RPGA, possibly at Gencon, DMs started ironing out the details of the alternate system, and by 1982 it had pollinated back to module writers for TSR.  Then there was some disagreement about whether it belonged in the Basic line, with some authors/editors using it right away and others avoiding it all the way into the 90s.  By 1987, though, the faults in a direct conversion to THAC0 (inability to hit things you could on the chart) had become obvious and were "patched" during the design of Second Edition by officially adopting the common house rule of always hitting on a natural 20.

D&D Third Edition (2002)
------------------------

3e brought about a drastic overhaul of nearly every die-roll mechanic, calling the new mechanic DC (Difficulty Class).  Saving throws, skills rolls, and even to-hit rolls became a matter of rolling 1d20, adding your bonuses, and trying to exceed the desired DC.  AC was divorced from its naval wargaming roots (1st-class armor being better than 3rd-class armor) and instead ascended as it got better.

On the one hand, this made the combat roll streamlined.  Our fighter needs to roll the goblin's AC (15) to hit it, adding 1 to the roll; in other words, a natural 14 or better.

On the other hand, this also lead to a linear progression of power and a proliferation of tiny bonuses to track.  That first-level fighter almost certainly isn't adding just +1; more likely +1 from Base Attack Bonus, +3 from Strength, +1 from a feat, etc.  It's not uncommon for a mid-level fighter to be adding +20 to an attack roll, and monsters have been scaled accordingly.  While it's mechanically identical to a low THAC0 combined with Strength and magic, it feels different during play to lump everything into a single bonus that overwhelms the variance range of the die it modifies.

Our archer example is quite similar to the THAC0 approach, but now the number and types of dragons has exploded (presumably to provide precise challenges for a party of any level).  

This approach of roll vs AC has remained through Pathfinder, 4e and 5e, for better or worse.

Which was better?
-----------------

The chart system was considered clumsy, particularly for the DM, who had to look up the right row for any given monster. But PCs could jot down their own target numbers (Basic even included it on the character sheet) for reasonable ranges.  Hidden in the Basic charts, however, were interesting subsystems: diminishing gains at higher levels; grace ranges in the form of target plateaus; different advancement systems for monsters.

THAC0 played comparatively quickly, once you got used to the math.  But advancement in both Advanced editions became linear and with THAC0 came the need for natural 20s, which opened the door for critical hits, then the need to balance those with confirming critical hits, and things got far more complicated than a table lookup.

By 3.x, the linearity was standardized into all areas; saving throws, bonuses from stats, costs to level, skill advancement, etc, etc.  Some of the heroic epic of the early editions was lost along the way.

.. [#basic] To avoid going down the rabbit hole of Moldvay vs Holmes basic, I'm treating everything from the 1977-ish Red Book onward as the same lineage.  This is mostly irrelevant to this mechanical deep-dive, but it's worth noting that AD&D didn't really come after "Basic" - AD&D was in parallel development for almost the entire Basic lifespan.  Even the Blue Book (1974) makes reference to the not-yet-printed AD&D game.


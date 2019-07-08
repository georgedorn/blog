On-the-fly Multiclassing Rules for BECMI / BX
#############################################

:date: 2019-07-08
:tags: rpg, D&D, history
:category: D&D, homebrew
:slug: multiclassing_in_basic

As much as I like Basic's simplicity, I miss the flexibility of multiclassing that 3.5 and 5e had.  5e's is even more reasonably balanced than 3.5's.

The key to the flexibility is not having to decide to be multiclass until after you've played a while.  1e and 2e's multiclass systems failed in this regard; you have to decide exactly what classes you were mixing when you start the character, and if you change your mind later you have to create a new character.

This optional multiclass system builds on Breeyark's excellent `Building a More Perfect Class <http://breeyark.org/building-a-more-perfect-class/>`_ series; that spreadsheet / calculator is essential for this additional feature.  In fact, traditional 1e/2e multiclassing is entirely possible using just that calculator, by picking the class features you want for your character as it is created.  This system adds the ability to buy additional features after the PC has been adventuring for a while, by spending XP to gradually become a new custom class.

How Multiclassing Works
=======================

At any time, a PC may decide to start learning a new set of class features.  A cleric might want to train like a fighter to gain the ability to use swords or have a d8 hit points.  A halfling might want to start learning thieving skills.

When this happens, use the class xp calculator to build in those new features, and generate another XP table for the character.  They don't change levels or classes yet, but new XP may be spent to level up those class features that were initially missing.  But until both classes are equal, buying up the new class features costs one level higher.  This also means that getting to level 1 in the new class costs the xp it would have taken to get from 1 to 2 if the character had always been this set of classes.

An example:  A 5th-level fighter decides to pick up spellcasting and *turn undead* like a cleric, and doesn't want to wait until level 9 to become a paladin.  His old, new, and difference chart looks like this:

===  ===== ===== ==== ==========
Lvl  Old   New   Diff Cumulative
===  ===== ===== ==== ==========
1    0     0     600  600
2    2000  2600  1200 1800
3    4000  5200  2400 4200
4    8000  10400 4800 9000
5    16000 20800 ---  ---
===  ===== ===== ==== ==========

He's already at 5th level, having obtained 16000xp.  To gain the powers of a level 1 cleric in addition to his existing fighter abilities, he'll need 600xp.  To gain the powers of a level 2 cleric, he'll need 1200xp more, and so on.  Once both classes are the same (level 5 in this case), his XP is set to 20,800 (5th level for the new class) plus any extra he had earned in Fighter before starting this exercise.  It cost 9000xp to get there, instead of just the 4800xp difference between level 5 fighter and level 5 fighter/cleric, but that's the cost of the flexibility.

It's not mandatory to advance in the new class continually.  When XP is earned, the player must decide whether to allocate it to the old class or the new class.  However, **so long as the player's classes are unequal, a 10% penalty is applied to all earned XP**.  (This is optional; it applies only if prime requisite xp penalties and bonuses are in use.)

Improved Hit Dice
-----------------

If the new class has a higher hit die than the old class, the player should replace the rolled hit points with a roll of the new hit die.  However, since most players don't track the hit points rolled at each level, they can instead opt to add the difference in average expected results, using the following table:

====== ====== =========
Old HD New HD +hp/level
====== ====== =========
1d4    1d6    1
1d4    1d8    2
1d6    1d8    1
====== ====== =========

If using the option d10 / d12 HD option from Breeyark, the pattern (half the difference in sides) holds; upgrading from a d4 to a d12 adds 4hp/level.

These extra hit points are only added when a level of a new class with a higher HD is being purchased; once the character's levels match, the new higher HD is rolled as normal.

Multiple Saving Throws
----------------------

In most cases, the player should choose which class's saving throws to use when creating the multiclass.  In the fighter/cleric example, I assumed the new class would keep the fighter saves.  Optionally, he could have used the cleric's saves, which are mostly better, though occasionally worse, for slightly more xp (2800 base).  If choosing a more expensive set of saving throws, the PC keeps any saves from the old class that were better than the new class, until advancement in the new class provides better saving throws.

For example, when the 5th-level fighter decides to gain levels of cleric, his saves are 10/11/12/13/14.  If he opts to pay the extra XP for cleric saves, the fighter saves are better until he reaches 5th-level in cleric.  At that point, he takes the best save for each class, or 9/10/12/13/13 (where a normal cleric of level 5 would have 9/10/12/14/13).  Then his saves continue improving as a cleric.

Overlapping Spell Levels / Level-based abilities
------------------------------------------------

If our example fighter/cleric reaches 9th level and decides to become a paladin, he'll be gaining cleric spells from two sources, as well as gaining the *turn undead* feature from two sources.  There are several options worth exploring, but it's unclear which is the most balanced:

1. **Ignore overlaps**: Ignore all but the best source of spells / class feature.  In the case of a paladin/cleric, the paladin still contributes *detect evil* and hirelings, but doesn't provide cleric spells or *turn undead*.
2. **Allow overlaps where possible**: Keep the best source, add extra memorization/castings per day from the other source, to a maximum of 9 in each level.  A paladin/cleric will get his level in cleric spells, but also his level / 3 in additional cleric spells.  For a 9th-level paladin/cleric, this just means an extra 2 first-level spells per day.  Around level 21, the 9-per-day limit starts to take effect for level 1 spells.  This is probably relatively balanced.  Because *turn undead* has no daily limit, this option ignores the paladin's *turn undead* contribution.
3. **Add sources together**: Take the best source of spells / class features, and for each other source, add levels equal to that source divided by the number of sources.  So our 9th-level paladin/cleric will cast spells or *turn undead* like a 10th-level cleric (9 from cleric, (9/3)/2 for paladin).  At level 12, he'll cast spells like a 14th-level cleric.  Around name level this isn't too bad (since it'll be adding 1-2 cleric levels but the PC has earned almost 1-2 levels of fighter in XP)  This is probably unbalanced at much higher levels, however.

Demihuman Limits
----------------

The class calculator makes it trivially easy to remove level limits from demihuman classes.  The Breeyark calculator suggests this adds 100xp to the base amount.  The DM should use caution when allowing this option, in particular if Magic-user spells are involved in the class.  The class feature of casting magic spells should be worth a lot more if the class can reach level 36, compared to the vanilla elf's level limit of 10.  This accounts for the main discrepancy in the Breeyark calculator, which thinks elves should have a base xp of 4100 (vs 4000) and magic-users should have a base xp of 2050 (vs 2500!).  Having unlimited access to magic-user spells is probably worth closer to 2000 base xp, instead of the calculator's 1600.

A similar adjustment might need to be made for demihuman clerics with no level limit.

It's also possible for a demihuman PC to reach maximum level and then decide to start spending that extra XP to remove the level limit; this will end up costing close to 50% more xp per level than just starting with that option, so it's not absurdly unbalanced.

Another consideration is demihuman hit dice.  The class calculator also makes it easy to change the hit dice or saving throws of a demihuman.  For instance, it's possible to make an elven fighter/magic-user with a d8 hit die instead of a d6.  It's up to the DM whether to allow this; it may make sense to require demihumans to stick to the hit die, saves and to-hit chart of the original vanilla class.


Some More Examples
------------------

Some common 1e multiclass options include dwarven fighter/thieves and elven fighter/mages.  Gnomish wizard/thief is also a textbook example in 1e, but we'd need to start by inventing the gnome class.

A **dwarven fighter/thief** has 2850xp/level, assuming the demihuman to-hit chart and weapon mastery, dwarven saving throws, all armor and dwarven-style limits on weapons.  The DM might choose to penalize the use of some thief skills in heavier armor, but there's no existing rules for it yet.  If the PC started as a vanilla dwarf and just wanted to add in thief skills, the chart up through level 5 looks like:

===  ===== ===== ====
Lvl  Old   New   Diff
===  ===== ===== ====
1    0     0     650
2    2200  2850  1300 
3    4400  5700  2600
4    8800  11400 5200 
5    17600 22800 ---
===  ===== ===== ====

To extend the chart, the Diff column is New - Old for the next row down.

An **elven fighter/mage** played this way must have started as a custom class to begin with, before mixing in the other class.  The new XP chart is the vanilla elf, but assuming the elf started as a fighter, with a base XP of 2200 (using Elf saves, Demihuman to-hit, fighter specials, elven racial abilities, name level limit).

===  ===== ===== ====
Lvl  Old   New   Diff
===  ===== ===== ====
1    0     0     1800
2    2200  4000  3600 
3    4400  8000  7200
4    8800  16000 14400 
5    17600 32000 ---
===  ===== ===== ====

This is a very expensive way to advance to a textbook elf, but the survivability of a fast-advancing fighting elf might be worth the extra cost in XP.


Conclusion
==========

This is still a work-in-progress, but I think it captures the spirit of what I'm trying to accomplish.  It adds much flexbility for long-lived characters who want to change up what they're doing, without needing to port in the somewhat wonky dual-class options from later editions, or forcing players to design their multiclass setup from the beginning.

There might be some balance issues I haven't considered; I've mostly thought about levels 1-5 since that is my favorite level of play.  It's entirely likely that something breaks badly around name level or higher.
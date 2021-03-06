import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'smuggler_1a':
		return

	actor.addSkill('expertise_sm_path_fake_goods_2')

	actor.addSkillMod('expertise_buff_duration_line_sm_false_hope', 1)
	actor.addSkillMod('expertise_delay_reduce_line_sm_false_hope', 1)

	addAbilities(core, actor, player)

	return

def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'smuggler_1a':
		return

	actor.removeSkill('expertise_sm_path_fake_goods_2')

	actor.removeSkillMod('expertise_buff_duration_line_sm_false_hope', 1)
	actor.removeSkillMod('expertise_delay_reduce_line_sm_false_hope', 1)

	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):


	return

def removeAbilities(core, actor, player):


	return

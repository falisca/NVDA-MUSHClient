# mushclient App Module for NVDA
# Developer 

import api
import review
import ui
import textInfos
import braille
import speech

import appModuleHandler
from scriptHandler import script
from globalCommands import commands, SCRCAT_TEXTREVIEW


class AppModule(appModuleHandler.AppModule):

    ##@@## number keys
    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:control+1")
    def script_review_bottom(self, gesture):
        commands.script_review_bottom(gesture)

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:control+2")
    def script_review_top(self, gesture):
        commands.script_review_top(gesture)

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:control+3")
    def script_review_startOfLine(self, gesture):
        commands.script_review_startOfLine(gesture)

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:control+4")
    def script_review_endOfLine(self, gesture):
        commands.script_review_endOfLine(gesture)

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:control+shift+1")
    def script_review_currentLine(self, gesture):
        commands.script_review_currentLine(gesture)

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:control+shift+2")
    def script_review_currentWord(self, gesture):
        commands.script_review_currentWord(gesture)

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:control+shift+3")
    def script_review_currentCharacter(self, gesture):
        commands.script_review_currentCharacter(gesture)

    ##@@## arrow keys

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:alt+UpArrow")
    def script_review_previousLine(self, gesture):
        commands.script_review_previousLine(gesture)

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:alt+DownArrow")
    def script_review_nextLine(self, gesture):
        commands.script_review_nextLine(gesture)

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:alt+LeftArrow")
    def script_review_previousWord(self, gesture):
        commands.script_review_previousWord(gesture)

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:alt+RightArrow")
    def script_review_nextWord(self, gesture):
        commands.script_review_nextWord(gesture)

    ##@@##

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:windows+alt+LeftArrow")
    def script_review_previousCharacter(self, gesture):
        commands.script_review_previousCharacter(gesture)

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:windows+alt+RightArrow")
    def script_review_nextCharacter(self, gesture):
        commands.script_review_nextCharacter(gesture)

    ##@@## other keys

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:control+L")
    def script_review_sayAll(self, gesture):
        commands.script_review_sayAll(gesture)

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:control+alt+space")
    def script_review_markStartForCopy(self, gesture):
        commands.script_review_markStartForCopy(gesture)
    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:control+shift+space")
    def script_review_copy(self, gesture):
        commands.script_review_copy(gesture)

    #category=inputCore.SCRCAT_MISC,
    @script(
        description=_("test"),
        gesture="kb:control+A")
    def script_navigatorObject_moveToFlatReviewAtObjectPosition(self, gesture):
        self.moveToFlatReviewAtObjectPosition(gesture)

    # inspired by the commands.script_reviewMode_next NVDA function
    def moveToFlatReviewAtObjectPosition(self, gesture):
        # set the flat review mode
        label = review.setCurrentMode('screen')
        # print and speak the text in the current position
        if label :
            pos=api.getReviewPosition().copy()
            pos.expand(textInfos.UNIT_LINE)
            braille.handler.setTether(braille.handler.TETHER_REVIEW, auto=True)
            speech.speakTextInfo(pos)


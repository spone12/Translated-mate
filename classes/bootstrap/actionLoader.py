from classes.enums.routes import Routes
from classes.services.translationHistory import TranslationHistory
from classes.factories.translate.TranslationUIMapper import TranslationUIMapper
from classes.actions.translateAction import TranslateAction
from classes.handlers.textChangeHandler import TextChangeHandler
from classes.actions.pronunciationAction import PronunciationAction
from classes.actions.pastSourceTextAction import PastSourceTextAction
from classes.actions.sourcePronunciationAction import SourcePronunciationAction
from classes.actions.saveTranslatedTextAction import SaveTranslatedTextAction
from classes.actions.reverseTranslateAction import ReverseTranslateAction
from classes.actions.copyTranslateAction import CopyTranslateAction
from classes.actions.sourceCopyTranslateAction import SourceCopyTranslateAction
from classes.actions.cleanTranslateAction import CleanTranslateAction
from classes.actions.goToRouteAction import GoToRouteAction
from classes.actions.previousTranslatitonAction import PreviousTranslationAction
from classes.actions.nextTranslatitonAction import NextTranslationAction


class ActionLoader:
    def __init__(self, context):
        self.context = context

    def bootstrap(self):
        """Load actions
        """
        
        # Action routes
        self.actionRoutes = {
            Routes.SAVED: GoToRouteAction(self.context.ui.TranslationViewWindow, self.context.navigator, Routes.SAVED, self.context.translationView.prepareWindow),
            Routes.FLASHCARDS: GoToRouteAction(self.context.ui.FlashCardsWindow, self.context.navigator, Routes.FLASHCARDS, self.context.flashCards.prepareWindow),
            Routes.SETTINGS: GoToRouteAction(self.context.ui.SettingsWindow, self.context.navigator, Routes.SETTINGS, self.context.settingsWindow.prepareWindow)
        }
        self.context.actionRouter.registerAll(self.actionRoutes)
        
        translationMapper = TranslationUIMapper(self.context.ui)
        history = TranslationHistory(self.context.ui, translationMapper)
        
        # Actions
        self.actions = [
            TranslateAction(self.context.ui, self.context.loadLang, self.context.navigator, history, translationMapper),
            SaveTranslatedTextAction(self.context.ui, self.context.db, self.context.actionRouter, translationMapper),
            PastSourceTextAction(self.context.ui),
            PronunciationAction(self.context.ui),
            SourcePronunciationAction(self.context.ui),
            CopyTranslateAction(self.context.ui),
            SourceCopyTranslateAction(self.context.ui),
            CleanTranslateAction(self.context.ui),
            ReverseTranslateAction(self.context.ui),
            PreviousTranslationAction(self.context.ui, history),
            NextTranslationAction(self.context.ui, history),
        ]

        # Handlers
        self.handlers = [
            TextChangeHandler(self.context.ui),
        ]
        
        # Triggers
        self.context.ui.actionExit.triggered.connect(self.context.menu.exitProgramm)
        self.context.ui.chooseTranslator.triggered.connect(self.context.loadLang.chooseTranslator)

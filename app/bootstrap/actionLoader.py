from app.enums.routes import Routes
from app.services.translationHistory import TranslationHistory
from app.factories.translate.TranslationUIMapper import TranslationUIMapper
from app.actions.translateAction import TranslateAction
from app.handlers.textChangeHandler import TextChangeHandler
from app.actions.pronunciationAction import PronunciationAction
from app.actions.pastSourceTextAction import PastSourceTextAction
from app.actions.sourcePronunciationAction import SourcePronunciationAction
from app.actions.saveTranslatedTextAction import SaveTranslatedTextAction
from app.actions.reverseTranslateAction import ReverseTranslateAction
from app.actions.copyTranslateAction import CopyTranslateAction
from app.actions.sourceCopyTranslateAction import SourceCopyTranslateAction
from app.actions.cleanTranslateAction import CleanTranslateAction
from app.actions.goToRouteAction import GoToRouteAction
from app.actions.previousTranslatitonAction import PreviousTranslationAction
from app.actions.nextTranslatitonAction import NextTranslationAction


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

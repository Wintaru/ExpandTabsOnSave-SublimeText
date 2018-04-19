"""ExpandTabsOnSave SublimeText plugin."""
import sublime_plugin


class ExpandTabsOnSave(sublime_plugin.EventListener):
    """Expand tabs / spaces on file save."""

    def on_pre_save(self, view):
        # Store the viewport position and selections.
        window = view.window()
        x, y = view.viewport_position()

        selections = view.sel()
        savedSelections = []

        for selection in selections:
            savedSelections.append(selection)

        view.selection.clear()

        """Run ST's 'expand_tabs' command when saving a file."""
        if view.settings().get('convert_tabspaces_on_save') == 1:
            if view.settings().get('translate_tabs_to_spaces') == 1:
                view.run_command('expand_tabs')
            else:
                view.run_command('unexpand_tabs')

        # Restore the viewport position and selections.
        window.focus_view(view)
        view.set_viewport_position([0, y], animate=False)
        view.selection.add_all(savedSelections)

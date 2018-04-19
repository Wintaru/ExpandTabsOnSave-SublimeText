"""ExpandTabsOnSave SublimeText plugin."""
import sublime_plugin


class ExpandTabsOnSave(sublime_plugin.EventListener):
    """Expand tabs / spaces on file save."""

    def on_pre_save(self, view):
        # Store the viewport position and selections.
        window = view.window()
        a_view = window.active_view()
        group = window.active_group()
        x, y = a_view.viewport_position()

        print('group: {0}'.format(str(group)))

        selections = a_view.sel()
        savedSelections = []

        for selection in selections:
            savedSelections.append(selection)

        a_view.selection.clear()

        """Run ST's 'expand_tabs' command when saving a file."""
        if a_view.settings().get('convert_tabspaces_on_save') == 1:
            if a_view.settings().get('translate_tabs_to_spaces') == 1:
                a_view.run_command('expand_tabs')
            else:
                a_view.run_command('unexpand_tabs')

        # Restore the viewport position and selections.
        window.focus_group(group)
        window.focus_view(a_view)
        a_view.set_viewport_position([0, y], animate=False)
        a_view.selection.add_all(savedSelections)

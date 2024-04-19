# -*- coding: utf-8 -*-
"""Compiler for Qt Designer .ui files"""

from __future__ import annotations

import os
import io
import subprocess
from enum import Enum, auto


EQUALS_SEPARATOR = " = "
WIDGETS_FIRST_LETTER = "Q"
WIDGETS_IDENTIFIER = f"{EQUALS_SEPARATOR}{WIDGETS_FIRST_LETTER}"
SELF_IDENTIFIER = "self."
SETUPUI_IDENTIFIER = "def setupUi("
DIALOG_IDENTIFIER = "Dialog"
MAINWINDOW_IDENTIFIER = "MainWindow"


class WindowType(Enum):
    invalid = auto()
    dialog = auto()
    mainWindow = auto()


def isWidgetDefinition(line: str) -> bool:
    return SELF_IDENTIFIER in line and WIDGETS_IDENTIFIER in line


def isSetupUiDefinition(line: str) -> bool:
    return SETUPUI_IDENTIFIER in line


def getWindowType(line: str) -> WindowType:
    if not isSetupUiDefinition(line):
        return WindowType.invalid

    if DIALOG_IDENTIFIER in line:
        return WindowType.dialog
    elif MAINWINDOW_IDENTIFIER in line:
        return WindowType.mainWindow
    else:
        return WindowType.invalid


def typeHintTextClassGenerator(
    widgets: list[str], windowType: WindowType, forceImportBaseClass: bool = False
) -> list[str]:

    # Format widget definition and supply type hinting
    for i, widget in enumerate(widgets):
        bare = widget.strip().replace(SELF_IDENTIFIER, "")
        typ = bare.split(EQUALS_SEPARATOR)[1].split("(")[0]
        hinted = bare.replace(EQUALS_SEPARATOR, f": {typ}{EQUALS_SEPARATOR}")
        widgets[i] = f"        {hinted}\n"

    # Insert headers
    widgets.insert(0, "\n\n\nimport typing\n")
    widgets.insert(1, "if typing.TYPE_CHECKING:\n\n")

    if windowType == WindowType.dialog:
        widgets.insert(
            2,
            (
                "    from PySide6.QtWidgets import QDialog\n"
                if forceImportBaseClass
                else ""
            ),
        )
        widgets.insert(3, "    class _TypeHint:\n")
        widgets.insert(4, '        """Auto-generated type hinting class"""\n\n')
        widgets.insert(5, "        Dialog: QDialog = QDialog()\n")
    elif windowType == WindowType.mainWindow:
        widgets.insert(
            2,
            (
                "    from PySide6.QtWidgets import QMainWindow\n"
                if forceImportBaseClass
                else ""
            ),
        )
        widgets.insert(3, "    class _TypeHint:\n")
        widgets.insert(4, '        """Auto-generated type hinting class"""\n\n')
        widgets.insert(5, "        MainWindow: QMainWindow = QMainWindow()\n")
    else:
        widgets.insert(2, "    class _TypeHint:\n")
        widgets.insert(3, '        """Auto-generated type hinting class"""\n\n')

    return widgets


def main():

    thisDir = os.path.dirname(__file__)
    pythonBaseDir = os.path.dirname(thisDir)

    uicExe = os.path.join(pythonBaseDir, "lib/PySide6/uic.exe").replace("\\", "/")
    uiDir = os.path.join(pythonBaseDir, "ui").replace("\\", "/")

    compiledFiles: list[str] = []

    # Compile UI files with UIC
    for root, dirs, files in os.walk(uiDir):
        for file in files:
            if not file.endswith(".ui"):
                continue

            fullPath = os.path.join(root, file).replace("\\", "/")
            outPath = fullPath.replace(".ui", "_ui.py")
            compiledFiles.append(outPath)

            print(f"Compiling {fullPath}")
            command = f'"{uicExe}" "{fullPath}" -g python -o "{outPath}"'
            result = subprocess.call(command, shell=True)
            if result == 0:
                print("Success")
            else:
                print("ERROR!")

    # Inject type hinting
    for file in compiledFiles:
        print(f"Generating type-hinting for {file}")
        widgets: list[str] = []
        windowType: WindowType = WindowType.invalid

        with open(file, "r+") as f:
            for line in f.readlines():
                # print(line)
                if isSetupUiDefinition(line):
                    windowType = getWindowType(line)
                elif isWidgetDefinition(line):
                    widgets.append(line)

            f.seek(0, io.SEEK_END)
            f.writelines(typeHintTextClassGenerator(widgets, windowType))

    print("Done")


if __name__ == "__main__":
    main()

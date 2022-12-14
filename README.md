# Font Size Per View 

A Sublime Text plugin to support adjusting the font size in each view individually (the default font size commands adjust it globally across all views).

<p align="center">
    <img
      src="https://user-images.githubusercontent.com/85039141/199656442-d40ec686-1354-4e3f-b1a0-2faca32a38cb.gif"
      alt="FontSizePerView plugin demo showing different font sizes between a couple of views"
      title="FontSizePerView plugin demo"
    >
</p>

## Installation

### Package Control

1. Open the command palette in Sublime Text (ctrl+shift+p by default).
1. Search for `Package Control: Install Package` and hit enter to execute the command.
1. Search for`Font Size Per View` in the list of displayed packages, then hit enter once it is focused to install the plugin.

The plugin will now be installed. 

[View package control page](https://packagecontrol.io/packages/Font%20Size%20Per%20View)

### Manual

#### Linux/Windows

Clone this repository into `~/.config/sublime-text/Packages/` named as `Font Size Per View`.

For example:
```console
$ git clone https://github.com/m-bartlett/SublimeFontSizePerView "~/.config/sublime-text/Packages/Font Size Per View"
```

#### MacOS

Clone this repository into `~/Library/Application Support/Sublime Text/Packages/` named as `Font Size Per View`.

For example:
```console
$ git clone https://github.com/m-bartlett/SublimeFontSizePerView "~/Library/Application Support/Sublime Text/Packages/Font Size Per View"
```

## Usage

### Command Palette

Using the command palette, query for any of these commands:
- `Font Size Per View: Increase View Font Size`
- `Font Size Per View: Decrease View Font Size`
- `Font Size Per View: Reset View Font Size`

**Note**: the `Reset View Font Size` command reads the `font_size` setting in your global user settings in `~/.config/sublime-text/Packages/User/Preferences.sublime-settings` to determine what font size to reset the view to.

### Default Keybinds

**Note**: These keybinds are commented out initially. To access a view to quickly edit your keybinding settings, click the context menu option `Preferences` > `Package Settings` > `Font Size Per View` > `Key Bindings`.

- `ctrl+alt+=` will call `adjust_font_size_per_view` with args `{"delta": 1}` which increases the active view's font size by 1 pt.
- `ctrl+alt+-` will call `adjust_font_size_per_view` with args `{"delta": -1}` which decreases the active view's font size by 1 pt.
- `ctrl+alt+0` will call `adjust_font_size_per_view` with args `{}` which resets the font size of the view back to the global `font_size` setting's value.

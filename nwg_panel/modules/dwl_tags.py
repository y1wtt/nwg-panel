#!/usr/bin/env python3
# from nwg_panel.tools import check_key, update_image

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk


class DwlTags(Gtk.EventBox):
    def __init__(self, output, dwl_data):
        Gtk.EventBox.__init__(self)
        self.output = output

        # move to settings later
        self.tags = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.title_limit = 55

        self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.add(self.box)
        self.label = Gtk.Label()
        self.tag_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.box.pack_end(self.label, False, False, 4)
        self.show_all()
        self.refresh(dwl_data)

    def refresh(self, dwl_data):
        if dwl_data:
            try:
                data = dwl_data[self.output]
                tags_string = data["tags"]
                tags = tags_string.split()
                non_empty_output_tags = int(tags[0])
                active_output_tag = int(tags[1])
                current_win_on_output_tags = int(tags[2])

                if self.tag_box:
                    self.tag_box.destroy()
                    self.tag_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
                    self.box.pack_start(self.tag_box, False, False, 4)

                cnt = 1
                for item in self.tags:
                    label = Gtk.Label()
                    self.tag_box.pack_start(label, False, False, 1)
                    label.set_text(item)

                    print("{} & {} == {}".format(cnt, non_empty_output_tags, cnt & non_empty_output_tags))
                    if cnt & non_empty_output_tags == 0:
                        label.set_property('name', "dwl-tag-free")
                    else:
                        label.set_property('name', "dwl-tag-occupied")
                    cnt += 1
                self.tag_box.show_all()

                layout = data["layout"]
                title = data["title"]
                if len(title) > self.title_limit:
                    title = title[:self.title_limit - 1]
                # selmon = data["selmon"] == "1"
                print("{} {} {}".format(tags_string, layout, title))
                self.label.set_text("{} {} {}".format(tags_string, layout, title))
            except KeyError:
                print("No data found for output {}".format(self.output))


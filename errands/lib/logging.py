# Copyright 2023 Vlad Krupinskii <mrvladus@yandex.ru>
# SPDX-License-Identifier: MIT

import datetime
import os
from gi.repository import GLib  # type:ignore
from __main__ import VERSION


class Log:
    """Logging class"""

    data_dir: str = os.path.join(GLib.get_user_data_dir(), "errands")
    log_file: str = os.path.join(data_dir, "log.txt")

    @classmethod
    def init(self):
        # Create data dir
        if not os.path.exists(self.data_dir):
            os.mkdir(self.data_dir)
        # Start new log
        self.empty(
            f"""
-------------------------------------------------
Starting Errands {VERSION} at "{datetime.datetime.now().strftime("%Y %d %B %H:%M:%S")}"
-------------------------------------------------
"""
        )

    @classmethod
    def debug(self, msg: str) -> None:
        print(f"\033[33;1m[DEBUG]\033[0m {msg}")
        self._log(self, f"[DEBUG] {msg}")

    @classmethod
    def error(self, msg: str) -> None:
        print(f"\033[31;1m[ERROR]\033[0m {msg}")
        self._log(self, f"[ERROR] {msg}")

    @classmethod
    def info(self, msg: str) -> None:
        print(f"\033[32;1m[INFO]\033[0m {msg}")
        self._log(self, f"[INFO] {msg}")

    @classmethod
    def empty(self, msg: str) -> None:
        print(msg)
        self._log(self, msg)

    def _log(self, msg: str) -> None:
        try:
            with open(self.log_file, "a") as f:
                f.write(msg + "\n")
        except OSError:
            self.error("Can't write to the log file")

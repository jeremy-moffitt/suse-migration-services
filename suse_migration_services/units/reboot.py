# Copyright (c) 2018 SUSE Linux LLC.  All rights reserved.
#
# This file is part of suse-migration-services.
#
# suse-migration-services is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# suse-migration-services is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with suse-migration-services. If not, see <http://www.gnu.org/licenses/>
#
# project
from suse_migration_services.command import Command
from suse_migration_services.logger import log


def main():
    """
    DistMigration reboot with new kernel
    """
    try:
        log.info('Running reboot service')
        Command.run(
            ['kexec', '--exec']
        )
    except Exception:
        # Uhh, we don't want to be here, but we also don't
        # want to be stuck in the migration live system.
        # Keep fingers crossed:
        log.warning('Forcing reboot')
        Command.run(
            ['reboot', '-f']
        )
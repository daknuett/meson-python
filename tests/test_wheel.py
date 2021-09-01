# SPDX-License-Identifier: EUPL-1.2

import re

import wheel.wheelfile


def test_contents(package_library, wheel_library):
    artifact = wheel.wheelfile.WheelFile(wheel_library)

    for name, regex in zip(artifact.namelist(), [
        r'library\.libs/libexample.*\.so',
    ] + list(map(re.escape, [
        'library-1.0.0.data/scripts/example',
        'library-1.0.0.dist-info/RECORD',
        'library-1.0.0.dist-info/WHEEL',
        'library-1.0.0.dist-info/METADATA',
    ]))):
        assert re.match(regex, name), f'`{name}` does not match `{regex}`'

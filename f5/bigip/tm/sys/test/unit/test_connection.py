# Copyright 2018 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import mock
import pytest

from f5.bigip.tm.sys import Connection
from f5.sdk_exception import UnsupportedOperation


@pytest.fixture
def fake_info():
    fake_sys = mock.MagicMock()
    return Connection(fake_sys)


def test_create_raises(fake_info):
    with pytest.raises(UnsupportedOperation) as EIO:
        fake_info.create()
    assert str(EIO.value) == "Operation not allowed on connections."

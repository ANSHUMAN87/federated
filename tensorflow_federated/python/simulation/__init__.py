# Copyright 2018, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The public API for experimenters running federated learning simulations."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_federated.python.simulation import datasets
from tensorflow_federated.python.simulation.client_data import ClientData
from tensorflow_federated.python.simulation.file_per_user_client_data import FilePerUserClientData
from tensorflow_federated.python.simulation.hdf5_client_data import HDF5ClientData
from tensorflow_federated.python.simulation.transforming_client_data import TransformingClientData

# Used by doc generation script.
_allowed_symbols = [
    "ClientData",
    "FilePerUserClientData",
    "HDF5ClientData",
    "TransformingClientData",
    "datasets",
]

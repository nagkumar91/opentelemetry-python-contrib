# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""GenAI event helpers (minimal).

Provides names and simple helper(s) for emitting GenAI-related events.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

try:
    from opentelemetry._events import Event
except Exception:  # pragma: no cover - fallback type
    Event = None  # type: ignore

OP_DETAILS_EVENT = "gen_ai.client.inference.operation.details"
EVAL_RESULT_EVENT = "gen_ai.evaluation.result"


def emit_operation_details_event(event_logger, attributes: Dict[str, Any]) -> None:
    """Emit a minimal operation details event if event logger available."""
    if not event_logger or Event is None:
        return
    try:
        event_logger.emit(Event(name=OP_DETAILS_EVENT, attributes=attributes))
    except Exception:  # pragma: no cover - defensive
        pass

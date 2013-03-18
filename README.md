Errplane
========

This library integrates your applications with [Errplane](http://errplane.com), a cloud-based tool for handling exceptions, custom metrics, uptime monitoring, and alerting.

Support
-------

Running into any issues? Get in touch with us at [support@errplane.com](mailto:support@errplane.com).

Configuration
----------------------

You can install the library using pip:

    pip install errplane

Then, import it into your app:

    from errplane import Errplane

And instantiate it with your API Key and the target Application ID:

	errplane = Errplane("YOUR_API_KEY", "APPLICATION_ID")

Sending Custom Metrics
------------------------

You can easily send a custom metric (with a default value of 1):

    errplane.report("metric_name")

Or, you can provide a different value and optionally, additional context:

    errplane.report("file_uploaded", value=file.bytes, context=file.name)

Heartbeats
----------

You can also start a heartbeat, which could be useful for monitoring background workers. This will start a thread which reports to the "background_worker" time series every 30 seconds:

    errplane.heartbeat("background_worker", 30)

Contributing
------------

We love contributions. Want to add support for something you don't already see here? Fork this repository and send us a pull request.

Copyright
---------

Copyright (c) 2012 Errplane, Inc.

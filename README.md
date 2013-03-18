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

	errplane = Errplane

Sending Custom Metrics
------------------------

Start by adding the gem to your Gemfile:

    gem "errplane"

Then, issue the following commands in your application's root directory:

    bundle
    script/generate errplane --api-key your-api-key-goes-here

This will create `config/initializers/errplane.rb` for you automatically. If you want to make sure that everything's working correctly, just run:

    bundle exec rake errplane:test

You should be able to view the exception at [http://errplane.com](http://errplane.com) and also receive an email notification of the test exception.

Contributing
------------

We love contributions. Want to add support for something you don't already see here? Fork this repository and send us a pull request.

Copyright
---------

Copyright (c) 2012 Errplane, Inc.

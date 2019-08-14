====================
Platform_utils
====================

Platform_utils is a library which provides several cross-platform utilities, including:

* path manipulation - allows you to do several things with paths including getting the path to store application data, creating the application data directory, checking whether the app is frozen, etc.
* clipboard - allows getting/setting clipboard text.
* idle - allows getting the user idle time on Windows.
* web_browser - allows opening a URL.
* process - allows killing processes on Windows and Unix.
* shell_integration - adds something to the context menu on Windows.
* blackhole - disables stdout/stderr when using py2exe.

Examples
==========

Check whether the app is frozen:
----------------------------------------


.. code-block:: python

    >>> import platform_utils.paths
    >>> platform_utils.paths.is_frozen()
    False

Find the recommended directory where user data files should be stored:
--------------------------------------------------------------------------------

.. code-block:: python

    >>> import platform_utils.paths
    >>> platform_utils.paths.app_data_path("app name")
    u'C:\\Users\\user\\AppData\\Roaming\\app name'

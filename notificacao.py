from win10toast import ToastNotifier

# initializing
toaster = ToastNotifier()

# parameters for notification
toaster.show_toast(
    "Notification!",
    "This is a notification",
    threaded = True,
    icon_path = None, # 'icon_32x32.ico',
)
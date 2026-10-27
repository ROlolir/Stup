using System;
using System.Diagnostics;
using System.Windows;

namespace StupApp
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            this.Loaded += MainWindow_Loaded;
        }

        private void MainWindow_Loaded(object sender, RoutedEventArgs e)
        {
            RunCheckScript();
        }

        private void RunCheckScript()
        {
            try
            {
                ProcessStartInfo start = new ProcessStartInfo
                {
                    FileName = "python",
                    Arguments = "check.py",
                    UseShellExecute = true,
                    CreateNoWindow = false
                };
                
                Process? process = Process.Start(start);
                if (process != null)
                {
                    process.WaitForExit();
                    if (process.ExitCode != 0)
                    {
                        MessageBox.Show("System check failed! Please fix the errors in terminal before playing.", "Stup Launcher - Error", MessageBoxButton.OK, MessageBoxImage.Warning);
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Could not run system check: " + ex.Message, "Stup Launcher - Error", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void RunPythonScript(string scriptName)
        {
            try
            {
                ProcessStartInfo start = new ProcessStartInfo
                {
                    FileName = "python",
                    Arguments = scriptName,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };
                Process.Start(start);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error launching script: " + ex.Message, "Stup Launcher - Error", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void BtnRoblox_Click(object sender, RoutedEventArgs e)
        {
            RunPythonScript("roblox.py");
        }

        private void BtnStudio_Click(object sender, RoutedEventArgs e)
        {
            RunPythonScript("studio.py");
        }
    }
}

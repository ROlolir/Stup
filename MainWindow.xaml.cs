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
            RunPythonScript("check.py", false);
        }

        private void RunPythonScript(string scriptName, bool isQuiet, string arguments = "")
        {
            try
            {
                ProcessStartInfo start = new ProcessStartInfo
                {
                    FileName = "python",
                    Arguments = isQuiet ? $"{scriptName} {arguments}" : scriptName,
                    UseShellExecute = !isQuiet,
                    CreateNoWindow = isQuiet
                };
                
                Process? process = Process.Start(start);
                if (!isQuiet && process != null)
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
                MessageBox.Show("Error launching script: " + ex.Message, "Stup Launcher - Error", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void BtnRoblox_Click(object sender, RoutedEventArgs e)
        {
            RunPythonScript("roblox.py", true);
        }

        private void BtnStudio_Click(object sender, RoutedEventArgs e)
        {
            RunPythonScript("studio.py", true);
        }

        private void BtnOpenSettings_Click(object sender, RoutedEventArgs e)
        {
            MainPanel.Visibility = Visibility.Collapsed;
            SettingsPanel.Visibility = Visibility.Visible;
        }

        private void BtnCloseSettings_Click(object sender, RoutedEventArgs e)
        {
            SettingsPanel.Visibility = Visibility.Collapsed;
            MainPanel.Visibility = Visibility.Visible;
        }

        private void BtnApplySkybox_Click(object sender, RoutedEventArgs e)
        {
            string path = TxtSkyboxPath.Text.Trim();
            if (string.IsNullOrEmpty(path))
            {
                MessageBox.Show("Please enter a valid file path!", "Stup Launcher", MessageBoxButton.OK, MessageBoxImage.Warning);
                return;
            }

            RunPythonScript("skybox.py", true, $"\"{path}\"");
            MessageBox.Show("Skybox update command sent!", "Stup Launcher", MessageBoxButton.OK, MessageBoxImage.Information);
        }
    }
}


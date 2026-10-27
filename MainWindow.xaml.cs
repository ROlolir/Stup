<Window x:Class="StupApp.MainWindow"
        xmlns="http://microsoft.com"
        xmlns:x="http://microsoft.com"
        Title="Stup Launcher" Height="350" Width="480"
        Background="#17191C" WindowStartupLocation="CenterScreen"
        ResizeMode="NoResize" BorderBrush="#1793D1" BorderThickness="1">
    
    <Grid>
        <Border Margin="20">
            <StackPanel VerticalAlignment="Center" HorizontalAlignment="Stretch">
                
                <TextBlock Text="STUP LAUNCHER" 
                           Foreground="#1793D1" 
                           FontSize="22" 
                           FontWeight="Black" 
                           HorizontalAlignment="Center" 
                           Margin="0,0,0,30"
                           LetterSpacing="4"/>

                <Button Name="BtnRoblox" Content="LAUNCH ROBLOX" Height="50" Margin="0,0,0,15"
                        Background="#212429" Foreground="#FFFFFF" FontSize="14" FontWeight="Bold"
                        Cursor="Hand" BorderBrush="#1793D1" BorderThickness="1" Click="BtnRoblox_Click">
                    <Button.Resources>
                        <Style TargetType="Border">
                            <Setter Property="CornerRadius" Value="2"/>
                        </Style>
                    </Button.Resources>
                </Button>

                <Button Name="BtnStudio" Content="LAUNCH ROBLOX STUDIO" Height="50" Margin="0,0,0,20"
                        Background="#212429" Foreground="#FFFFFF" FontSize="14" FontWeight="Bold"
                        Cursor="Hand" BorderBrush="#333333" BorderThickness="1" Click="BtnStudio_Click">
                    <Button.Resources>
                        <Style TargetType="Border">
                            <Setter Property="CornerRadius" Value="2"/>
                        </Style>
                    </Button.Resources>
                </Button>

                <TextBlock Text="SYSTEM READY" 
                           Foreground="#444444" 
                           FontSize="10" 
                           FontWeight="Medium" 
                           HorizontalAlignment="Center" 
                           LetterSpacing="2"/>
                
            </StackPanel>
        </Border>
    </Grid>
</Window>

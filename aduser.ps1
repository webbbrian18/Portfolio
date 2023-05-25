Add-Type -AssemblyName System.Windows.Forms

# Create the pop-up form and its controls
$form = New-Object System.Windows.Forms.Form
$form.Text = "New User Creation"
$form.Width = 300
$form.Height = 200

$firstnameLabel = New-Object System.Windows.Forms.Label
$firstnameLabel.Text = "First Name:"
$firstnameLabel.Location = New-Object System.Drawing.Point(10, 20)
$form.Controls.Add($firstnameLabel)

$firstnameBox = New-Object System.Windows.Forms.TextBox
$firstnameBox.Location = New-Object System.Drawing.Point(100, 20)
$form.Controls.Add($firstnameBox)

$lastnameLabel = New-Object System.Windows.Forms.Label
$lastnameLabel.Text = "Last Name:"
$lastnameLabel.Location = New-Object System.Drawing.Point(10, 50)
$form.Controls.Add($lastnameLabel)

$lastnameBox = New-Object System.Windows.Forms.TextBox
$lastnameBox.Location = New-Object System.Drawing.Point(100, 50)
$form.Controls.Add($lastnameBox)

$usernameLabel = New-Object System.Windows.Forms.Label
$usernameLabel.Text = "Username:"
$usernameLabel.Location = New-Object System.Drawing.Point(10, 80)
$form.Controls.Add($usernameLabel)

$usernameBox = New-Object System.Windows.Forms.TextBox
$usernameBox.Location = New-Object System.Drawing.Point(100, 80)
$form.Controls.Add($usernameBox)

$okButton = New-Object System.Windows.Forms.Button
$okButton.Text = "OK"
$okButton.Location = New-Object System.Drawing.Point(75, 120)
$okButton.DialogResult = [System.Windows.Forms.DialogResult]::OK
$form.AcceptButton = $okButton
$form.Controls.Add($okButton)

$cancelButton = New-Object System.Windows.Forms.Button
$cancelButton.Text = "Cancel"
$cancelButton.Location = New-Object System.Drawing.Point(155, 120)
$cancelButton.DialogResult = [System.Windows.Forms.DialogResult]::Cancel
$form.CancelButton = $cancelButton
$form.Controls.Add($cancelButton)

# Show the pop-up form and get the entered values
$result = $form.ShowDialog()

if ($result -eq [System.Windows.Forms.DialogResult]::OK) {
    # Set the variables for the new user
    $firstname = $firstnameBox.Text
    $lastname = $lastnameBox.Text
    $username = $usernameBox.Text
    $password = ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force
    $ou = "OU=Users,DC=example,DC=com"

    # Check if the user already exists
    if (Get-ADUser -Filter { SamAccountName -eq $username }) {
        Write-Output "User $username already exists"
    } else {
        # Create the new user object
        $newuser = New-ADUser `
          -GivenName $firstname `
          -Surname $lastname `
          -UserPrincipalName "$username@example.com" `
          -SamAccountName $username `
          -AccountPassword $password `
          -Enabled $true `
          -Path $ou

        # Set additional properties for the new user
        Set-ADUser $newuser `
          -DisplayName "$firstname $lastname" `
          -EmailAddress "$username@example.com" `
          -Description "New user account"
          
        # Display the details of the new user
        Write-Output "User $username created"
    }
}

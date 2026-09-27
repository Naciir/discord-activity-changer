
import pypresence
import time
import sys

# This is a placeholder - replace with the actual Discord Application ID
CLIENT_ID = "1447377"


def set_presence():
    # Validate Application ID
    if CLIENT_ID == "your_application_id_here":
        print("ERROR: You need to replace 'your_application_id_here' with your actual Application ID!")
        print("\nSteps to get your Application ID:")
        print("1. Go to https://discord.com/developers/applications")
        print("2. Click 'New Application' and name it")
        print("3. Copy the Application ID from the General Information page")
        print("4. Replace CLIENT_ID in this script with that number")
        sys.exit(1)
    
    try:
        print("Attempting to connect to Discord...")
        RPC = pypresence.Presence(CLIENT_ID)
        RPC.connect()
        
        print("✓ Connected to Discord successfully!")
        print("\nSetting presence to 'Where Winds Meet'...")
        
        # Update presence with more details
        RPC.update(
            state="In Game",
            details="Playing Where Winds Meet",
            start=int(time.time()),
        )
        
        print("✓ Presence set successfully!")
        print("\n" + "="*60)
        print("HOW TO CHECK IF IT'S WORKING:")
        print("1. Right-click your profile picture in Discord")
        print("2. Click 'View Profile'")
        print("3. Look for 'Where Winds Meet' in your activity section")
        print("   OR ask a friend to check your profile")
        print("\nNOTE: It won't show in your status bar at the bottom!")
        print("="*60)
        print("\nScript is running... Press Ctrl+C to stop\n")
        
        # Keep the script running
        while True:
            time.sleep(15)
            
    except pypresence.exceptions.InvalidID:
        print("\n❌ ERROR: Invalid Application ID!")
        print("Make sure you're using the correct Application ID from Discord Developer Portal")
        print("The ID should be 18-19 digits long (like: 1234567890123456789)")
    except pypresence.exceptions.DiscordNotFound:
        print("\n❌ ERROR: Discord is not running!")
        print("Please make sure Discord is open and try again.")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print(f"Error type: {type(e).__name__}")
    finally:
        try:
            RPC.close()
            print("\nDisconnected from Discord.")
        except:
            pass

if __name__ == "__main__":
    print("╔═══════════════════════════════════════════════════╗")
    print("║  Discord Rich Presence - Where Winds Meet        ║")
    print("╔═══════════════════════════════════════════════════╗")
    print()
    set_presence()

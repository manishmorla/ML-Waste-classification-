# 📁 How to Organize Your Training Data

## Quick Start

### Option 1: Use the Helper Script (Easiest) ✅

I've created a helper script to organize your images:

```bash
python organize_data.py --interactive
```

This will:
- ✅ Create the `Data` folder structure
- ✅ Show you each image one by one
- ✅ Let you categorize each image (Organic/Non-Organic)
- ✅ Copy images to the correct folders automatically

**How it works:**
1. Run the script
2. For each image, type:
   - `o` or `1` = ORGANIC
   - `n` or `2` = NONORGANIC
   - `s` = Skip this image
   - `q` = Quit
3. Images are automatically copied to the right folders!

### Option 2: Manual Organization

**Step 1: Create folders**
```bash
python organize_data.py
# Choose option 2
```

Or manually:
```bash
mkdir Data
mkdir Data\ORGANIC
mkdir Data\NONORGANIC
```

**Step 2: Copy images manually**

1. Open File Explorer
2. Go to `test images` folder
3. Look at each image and decide:
   - **ORGANIC**: Food waste, leaves, paper, biodegradable items
   - **NONORGANIC**: Plastic, metal, glass, synthetic materials
4. Copy images to the appropriate folder:
   - `Data\ORGANIC\` for organic waste
   - `Data\NONORGANIC\` for non-organic waste

## What Goes Where?

### ORGANIC Folder (Biodegradable)
- 🍎 Food scraps (fruits, vegetables, leftovers)
- 🍃 Leaves and garden waste
- 📄 Paper and cardboard (if biodegradable)
- 🌿 Natural materials
- 🥚 Eggshells
- ☕ Coffee grounds

### NONORGANIC Folder (Non-biodegradable)
- 🥤 Plastic bottles and containers
- 🥫 Metal cans and foil
- 🍾 Glass bottles and jars
- 🔋 Batteries
- 💻 Electronics
- 🧴 Synthetic materials

## Tips for Better Training

1. **Balance**: Try to have roughly equal numbers in each folder
   - Example: 50 ORGANIC + 50 NONORGANIC = Good!
   - Example: 10 ORGANIC + 90 NONORGANIC = Not ideal

2. **Quality**: Use clear, representative images
   - ✅ Good: Clear, well-lit, single item
   - ❌ Bad: Blurry, dark, multiple items mixed

3. **Quantity**: More is better!
   - Minimum: 20-30 images per category
   - Recommended: 50+ images per category
   - Ideal: 100+ images per category

4. **Variety**: Include different types of waste
   - Different angles
   - Different lighting
   - Different backgrounds

## Quick Organization Workflow

### Using the Script:

```bash
# Step 1: Run interactive organizer
python organize_data.py --interactive

# Step 2: Categorize images as they appear
# Type 'o' for organic, 'n' for non-organic

# Step 3: When done, train the model
python backend/train_model.py
```

### Manual Workflow:

1. **Create folders** (if not done):
   ```bash
   mkdir Data\ORGANIC Data\NONORGANIC
   ```

2. **Open two File Explorer windows**:
   - Window 1: `test images` folder
   - Window 2: `Data` folder

3. **Review and drag images**:
   - Look at each image
   - Drag to `ORGANIC` or `NONORGANIC` folder
   - Be consistent with categorization

4. **Verify**:
   - Check both folders have images
   - Aim for balanced numbers

5. **Train**:
   ```bash
   python backend/train_model.py
   ```

## Example Structure

After organization, your folder should look like:

```
ML-Waste-classification-/
├── Data/
│   ├── ORGANIC/
│   │   ├── apple1.jpg
│   │   ├── leaves1.jpg
│   │   ├── paper1.jpg
│   │   └── ... (more organic images)
│   └── NONORGANIC/
│       ├── plastic1.jpg
│       ├── metal1.jpg
│       ├── glass1.jpg
│       └── ... (more non-organic images)
├── test images/
│   └── ... (original images)
└── backend/
    └── models/
        └── RF_Classifier.pkl (after training)
```

## Verification

After organizing, verify your data:

```bash
# Count images in each folder
dir Data\ORGANIC /b | find /c ".jpg"
dir Data\NONORGANIC /b | find /c ".jpg"
```

Or check manually in File Explorer.

## Common Questions

**Q: How many images do I need?**
A: Minimum 20-30 per category, but 50+ is better for good accuracy.

**Q: What if I'm not sure if something is organic?**
A: When in doubt, skip it or make your best guess. The model will learn from patterns.

**Q: Can I add more images later?**
A: Yes! Just add them to the folders and retrain the model.

**Q: What image formats are supported?**
A: JPG, PNG, JPEG, BMP

**Q: Can I use the same image in both folders?**
A: No, each image should only be in one category.

## Next Steps

Once organized:

1. ✅ Verify both folders have images
2. ✅ Run training: `python backend/train_model.py`
3. ✅ Wait for training to complete
4. ✅ Start backend: `python backend/app.py`
5. ✅ Test in frontend!

---

**Ready to organize?** Run: `python organize_data.py --interactive`

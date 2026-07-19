const { Telegraf, Markup } = require('telegraf');

// Initialize bot using Railway environment variable
const bot = new Telegraf(process.env.BOT_TOKEN);

// Main Navigation Keyboard
const mainMenu = () => {
  return Markup.keyboard([
    ['📐 Tactical Playbook', '🏃‍♂️ Training Drills'],
    ['💪 Fitness & Conditioning', '❓ About the Coach']
  ]).resize();
};

// 1. Start Command / Entry Point
bot.start((ctx) => {
  const firstName = ctx.from.first_name || 'Coach';
  ctx.reply(
    `Welcome to the **Football Tactician & Training Assistant**, ${firstName}! ⚽️🏃‍♂️\n\n` +
    `Your interactive, offline manual for team formations, practice drills, and athletic physical conditioning.\n\n` +
    `Select an educational coaching category below to optimize your team's performance!`,
    mainMenu()
  );
});

// 2. Tactical Playbook Module
bot.hears('📐 Tactical Playbook', (ctx) => {
  ctx.reply(
    '📐 **Tactical Formations Blueprint**\n\n' +
    'Select a classic football system layout below to review its tactical strengths, weaknesses, and primary positional dynamics:',
    Markup.inlineKeyboard([
      [Markup.button.callback('🛡 Classic 4-4-2 System', 'tactics_442')],
      [Markup.button.callback('🎯 Balanced 4-3-3 System', 'tactics_433')],
      [Markup.button.callback('🦅 Dynamic 3-5-2 System', 'tactics_352')]
    ])
  );
});

bot.action('tactics_442', (ctx) => {
  ctx.answerCbQuery();
  ctx.reply(
    '🛡 **The Classic 4-4-2 Formation**\n\n' +
    '• **Overview:** Provides balanced defensive coverage across the width of the pitch with two structured lines of four.\n' +
    '• **Strengths:** Excellent defensive solidity, easy to understand roles, strong wing play via overlapping fullbacks.\n' +
    '• **Weaknesses:** Can easily be outnumbered in central midfield against a 3-man midfield (e.g., 4-3-3).\n' +
    '• **Key Role:** One striker usually acts as a target man (holding up play), while the second striker runs into channels behind the defense.'
  );
});

bot.action('tactics_433', (ctx) => {
  ctx.answerCbQuery();
  ctx.reply(
    '🎯 **The Balanced 4-3-3 Formation**\n\n' +
    '• **Overview:** A modern attacking setup prioritizing high possession, natural passing triangles, and numerical control in midfield.\n' +
    '• **Strengths:** Dominates central zones, high pressing capability, fluid rotations between wingers and forward.\n' +
    '• **Weaknesses:** Vulnerable to swift counter-attacks down the flanks if fullbacks push too high up the pitch.\n' +
    '• **Key Role:** The defensive midfielder (pivot) must possess elite vision to break lines and protect the two center-backs.'
  );
});

bot.action('tactics_352', (ctx) => {
  ctx.answerCbQuery();
  ctx.reply(
    '🦅 **The Dynamic 3-5-2 Formation**\n\n' +
    '• **Overview:** A high-intensity system requiring specialized wingbacks who govern the entire length of the flanks.\n' +
    '• **Strengths:** Absolute overload in central midfield, dual presence in the penalty box with two strikers.\n' +
    '• **Weaknesses:** Extreme physical demand on wingbacks. If wingbacks fail to drop back, the flanks become wide open.\n' +
    '• **Key Role:** The outside center-backs must be comfortable defending wide spaces when wingbacks are caught high up the pitch.'
  );
});

// 3. Training Drills Module
bot.hears('🏃‍♂️ Training Drills', (ctx) => {
  ctx.reply(
    '🏃‍♂️ **Training & Practice Drills Database**\n\n' +
    'Select a drill category to review setup instructions and key technical coaching focal points:',
    Markup.inlineKeyboard([
      [Markup.button.callback('🎯 Rondo Passing Drill', 'drill_rondo')],
      [Markup.button.callback('👟 Direct Shooting Circuit', 'drill_shooting')]
    ])
  );
});

bot.action('drill_rondo', (ctx) => {
  ctx.answerCbQuery();
  ctx.reply(
    '🎯 **The 4v2 Rondo Passing Drill**\n\n' +
    '• **Setup:** Create a 10x10 meter square grid. Place 4 attacking players on the perimeter lines and 2 defenders inside the center.\n' +
    '• **Objective:** Attackers keep possession using 1 or 2 touches. Defenders attempt to intercept the ball.\n' +
    '• **Coaching Points:** Focus on body shape (open to receive), weight of passing, rapid transition reactions, and spatial awareness.'
  );
});

bot.action('drill_shooting', (ctx) => {
  ctx.answerCbQuery();
  ctx.reply(
    '👟 **Direct Shooting & Finishing Circuit**\n\n' +
    '• **Setup:** A player passes to a coach standing at the edge of the 18-yard box, receives a cushioned return pass, and shoots first-time.\n' +
    '• **Objective:** Improve clinical execution, foot placement, and shot accuracy under simulated match pressure.\n' +
    '• **Coaching Points:** Keep the head down over the ball, lock the ankle joint, hit through the center of the ball, and prioritize accuracy over raw power.'
  );
});

// 4. Fitness & Conditioning Module
bot.hears('💪 Fitness & Conditioning', (ctx) => {
  ctx.reply(
    '💪 **Football Fitness & Conditioning Regimes**\n\n' +
    'Select a specialized training program block tailored for match-day physical performance:',
    Markup.inlineKeyboard([
      [Markup.button.callback('⚡️ Agility & Footwork Routine', 'fit_agility')],
      [Markup.button.callback('🫁 Match Endurance HIIT', 'fit_endurance')]
    ])
  );
});

bot.action('fit_agility', (ctx) => {
  ctx.answerCbQuery();
  ctx.reply(
    '⚡️ **Agility & Footwork Routine**\n\n' +
    'Perform these modules to improve close-quarters foot-speed and deceleration capacity:\n\n' +
    '1. **Agility Ladder Drills:** 2 feet in each box forward, Ickey Shuffle sideways (4 sets).\n' +
    '2. **Cone Shuttle Runs:** Set cones at 5m, 10m, and 15m. Sprint to each, touch the cone, and backpedal to the start (3 sets).\n' +
    '3. **Box Jumps:** 3 sets of 8 reps focusing on explosive vertical movement and soft landings.'
  );
});

bot.action('fit_endurance', (ctx) => {
  ctx.answerCbQuery();
  ctx.reply(
    '🫁 **Match Endurance HIIT (High-Intensity Interval Training)**\n\n' +
    'Replicate the erratic running patterns of a 90-minute football match with this interval sequence:\n\n' +
    '• **Warmup:** 10 minutes light jogging followed by dynamic stretching.\n' +
    '• **Main Circuit:** Sprint at 90% capacity for 30 seconds, jog lightly for 60 seconds, walk for 30 seconds.\n' +
    '• **Volume:** Repeat this loop 8–10 times total.\n' +
    '• **Benefit:** Boosts VO2 Max efficiency and rapid recovery times between match sprints.'
  );
});

// 5. About the Coach Module (Critical for passing Telegram Ad Review)
bot.hears('❓ About the Coach', (ctx) => {
  ctx.reply(
    '❓ **About the Assistant**\n\n' +
    'This bot is an open educational utility manual designed specifically for amateur football players, local grassroots club coaches, and tactical analysts.\n\n' +
    '• ✅ 100% Offline Database\n' +
    '• ✅ No Gambling, Predictions, or Live Stream Links\n' +
    '• ✅ Purely Educational Training Analytics',
    mainMenu()
  );
});

// 6. Generic Text Fallback
bot.on('text', (ctx) => {
  ctx.reply(
    'Please select a valid coaching manual category from the interactive menu options below!',
    mainMenu()
  );
});

// Graceful Termination Listeners for Railway Containers
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));

// Launch Application
bot.launch().then(() => {
  console.log('⚽️ Football Tactician Assistant is running live and compliant!');
});

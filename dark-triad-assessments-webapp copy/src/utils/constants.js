// Constants for the Dark Triad Assessments web application

export const ASSESSMENT_TYPES = {
  SDT3: 'Short Dark Triad',
  SDT4: 'Short Dark Tetrad',
  MACHIV: 'MACH-IV',
  DIRTY_DOZENS: 'Dirty Dozen',
  SECS: 'Social and Economic Conservatism Scale',
  SBA: 'Social Behavior Assessment',
};

export const TRAIT_TYPES = {
  NARCISSISM: 'Narcissism',
  MACHIAVELLIANISM: 'Machiavellianism',
  PSYCHOPATHY: 'Psychopathy',
  SADISM: 'Sadism', // For SDT4
};

export const LIKERT_SCALE = [
  { value: 1, label: 'Strongly Disagree' },
  { value: 2, label: 'Disagree' },
  { value: 3, label: 'Neutral' },
  { value: 4, label: 'Agree' },
  { value: 5, label: 'Strongly Agree' },
];

export const SDT4_QUESTIONS = [
  { id: 1, text: "It's not wise to tell your secrets.", trait: TRAIT_TYPES.MACHIAVELLIANISM },
  { id: 2, text: "I like to use clever manipulation to get my way.", trait: TRAIT_TYPES.MACHIAVELLIANISM },
  { id: 3, text: "Whatever it takes, you must get the important people on your side.", trait: TRAIT_TYPES.MACHIAVELLIANISM },
  { id: 4, text: "Avoid direct conflict with others because they may be useful in the future.", trait: TRAIT_TYPES.MACHIAVELLIANISM },
  { id: 5, text: "It's wise to keep track of information that you can use against people later.", trait: TRAIT_TYPES.MACHIAVELLIANISM },
  { id: 6, text: "You should wait for the right time to get back at people.", trait: TRAIT_TYPES.MACHIAVELLIANISM },
  { id: 7, text: "There are things you should hide from other people because they don't need to know.", trait: TRAIT_TYPES.MACHIAVELLIANISM },
  { id: 8, text: "People see me as a natural leader.", trait: TRAIT_TYPES.NARCISSISM },
  { id: 9, text: "I have a unique talent for persuading people.", trait: TRAIT_TYPES.NARCISSISM },
  { id: 10, text: "Group activities tend to be dull without me.", trait: TRAIT_TYPES.NARCISSISM },
  { id: 11, text: "I know that I am special because everyone keeps telling me so.", trait: TRAIT_TYPES.NARCISSISM },
  { id: 12, text: "I have a great deal of natural talent.", trait: TRAIT_TYPES.NARCISSISM },
  { id: 13, text: "I like to show off every now and then.", trait: TRAIT_TYPES.NARCISSISM },
  { id: 14, text: "I'm likely to become a future star in some area.", trait: TRAIT_TYPES.NARCISSISM },
  { id: 15, text: "People who mess with me always regret it.", trait: TRAIT_TYPES.PSYCHOPATHY },
  { id: 16, text: "You should take advantage of other people before they do it to you.", trait: TRAIT_TYPES.PSYCHOPATHY },
  { id: 17, text: "People often say I'm out of control.", trait: TRAIT_TYPES.PSYCHOPATHY },
  { id: 18, text: "I sometimes get into trouble for breaking rules.", trait: TRAIT_TYPES.PSYCHOPATHY },
  { id: 19, text: "I tend to fight against authorities and their rules.", trait: TRAIT_TYPES.PSYCHOPATHY },
  { id: 20, text: "I've been in more fights than most people of my age and gender.", trait: TRAIT_TYPES.PSYCHOPATHY },
  { id: 21, text: "I tend to dive in, then ask questions later.", trait: TRAIT_TYPES.PSYCHOPATHY },
  { id: 22, text: "I love to watch YouTube clips of people fighting.", trait: TRAIT_TYPES.SADISM },
  { id: 23, text: "I enjoy watching violent sports.", trait: TRAIT_TYPES.SADISM },
  { id: 24, text: "Some people deserve to suffer.", trait: TRAIT_TYPES.SADISM },
  { id: 25, text: "Just for kicks, I've said mean things on social media.", trait: TRAIT_TYPES.SADISM },
  { id: 26, text: "I know how to hurt someone with words alone.", trait: TRAIT_TYPES.SADISM },
  { id: 27, text: "I enjoy making jokes at the expense of others.", trait: TRAIT_TYPES.SADISM },
  { id: 28, text: "I have fantasies about hurting people who have wronged me.", trait: TRAIT_TYPES.SADISM },
];

export const DIRTY_DOZEN_LIKERT_SCALE = [
  { value: 1, label: 'Strongly Disagree' },
  { value: 2, label: 'Disagree' },
  { value: 3, label: 'Somewhat Disagree' },
  { value: 4, label: 'Neutral' },
  { value: 5, label: 'Somewhat Agree' },
  { value: 6, label: 'Agree' },
  { value: 7, label: 'Strongly Agree' },
];

export const DIRTY_DOZEN_QUESTIONS = [
  { id: 1, text: "I tend to manipulate others to get my way.", trait: TRAIT_TYPES.MACHIAVELLIANISM },
  { id: 2, text: "I tend to lack remorse.", trait: TRAIT_TYPES.PSYCHOPATHY },
  { id: 3, text: "I tend to want others to admire me.", trait: TRAIT_TYPES.NARCISSISM },
  { id: 4, text: "I tend to be unconcerned with the morality of my actions.", trait: TRAIT_TYPES.PSYCHOPATHY },
  { id: 5, text: "I have used deceit or lied to get my way.", trait: TRAIT_TYPES.MACHIAVELLIANISM },
  { id: 6, text: "I tend to be callous or insensitive.", trait: TRAIT_TYPES.PSYCHOPATHY },
  { id: 7, text: "I have used flattery to get my way.", trait: TRAIT_TYPES.MACHIAVELLIANISM },
  { id: 8, text: "I tend to seek prestige or status.", trait: TRAIT_TYPES.NARCISSISM },
  { id: 9, text: "I tend to be cynical.", trait: TRAIT_TYPES.PSYCHOPATHY },
  { id: 10, text: "I tend to exploit others toward my own end.", trait: TRAIT_TYPES.MACHIAVELLIANISM },
  { id: 11, text: "I tend to expect special favors from others.", trait: TRAIT_TYPES.NARCISSISM },
  { id: 12, text: "I want others to pay attention to me.", trait: TRAIT_TYPES.NARCISSISM },
];

export const SECS_QUESTIONS = [
  { id: 1, text: "Abortion", trait: "SOCIAL", reverse: true },
  { id: 2, text: "Limited government", trait: "ECONOMIC" },
  { id: 3, text: "Military and national security", trait: "SOCIAL" },
  { id: 4, text: "Religion", trait: "SOCIAL" },
  { id: 5, text: "Welfare benefits", trait: "ECONOMIC", reverse: true },
  { id: 6, text: "Gun ownership", trait: "ECONOMIC" },
  { id: 7, text: "Traditional marriage", trait: "SOCIAL" },
  { id: 8, text: "Traditional values", trait: "SOCIAL" },
  { id: 9, text: "Fiscal responsibility", trait: "ECONOMIC" },
  { id: 10, text: "Business", trait: "ECONOMIC" },
  { id: 11, text: "The family unit", trait: "SOCIAL" },
  { id: 12, text: "Patriotism", trait: "SOCIAL" },
];

export const SBA_QUESTIONS = [
  { id: 1, text: "I act wild and crazy." },
  { id: 2, text: "I am good at making impromptu speeches." },
  { id: 3, text: "I have wanted to be a stand-up comedian." },
  { id: 4, text: "I make big physical movements whenever I get excited." },
  { id: 5, text: "I make a lot of hand motions when I talk." },
  { id: 6, text: "I mostly listen to people in conversations.", reverse: true },
  { id: 7, text: "I often feel lucky." },
  { id: 8, text: "When I was a child, I put on fake concerts and plays with my friends." },
  { id: 9, text: "I prefer to eat alone.", reverse: true },
  { id: 10, text: "I have not been joyful for quite some time.", reverse: true },
  { id: 11, text: "I would never audition to be on a game show.", reverse: true },
  { id: 12, text: "I hate to ask for help.", reverse: true },
  { id: 13, text: "I want a huge social circle." },
  { id: 14, text: "I am a touchy feely person." },
  { id: 15, text: "I am a bundle of joy." },
  { id: 16, text: "I do not like to get my picture taken.", reverse: true },
  { id: 17, text: "I tire out quickly.", reverse: true },
  { id: 18, text: "I laugh a lot." },
  { id: 19, text: "I am a high status person." },
  { id: 20, text: "I like pranks." },
  { id: 21, text: "I am brave." },
  { id: 22, text: "I was an outcast in school.", reverse: true },
  { id: 23, text: "I don't mind being the center of attention." },
  { id: 24, text: "I am quiet around strangers.", reverse: true },
  { id: 25, text: "I hate shopping.", reverse: true },
];

// Add more constants as needed
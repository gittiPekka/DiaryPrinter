CREATE TABLE IF NOT EXISTS "days" (
	"id"	INTEGER NOT NULL,
	"sleepingTimeHours"	INTEGER,
	"sleepingTimeMinutes"	INTEGER,
	"wakeupTimeHours"	INTEGER,
	"wakeupTimeMinutes"	INTEGER,
	"night"	TEXT,
	"breakfast"	TEXT,
	"morning"	TEXT,
	"lunch"	TEXT,
	"afternoon"	TEXT,
	"dinner"	TEXT,
	"evening"	TEXT,
	PRIMARY KEY("id")
);


/*
 * Solution for Advent of Code 2023, Day 04
 * https://adventofcode.com/2023/day/04
 */

import * as fs from "fs";

function solveDay04(filename: string ="./input.txt"): [number, number]|string {
    try {
        const data: string = fs.readFileSync(filename, 'utf8');
        const rows: string[] = data.split("\n");
        let totalPoints: number = 0;
        const scratchcards: {} = {};

        rows.forEach((row: string, idxRow: number) => {
            const allValues: string[] = row.split("|");
            const card: string = allValues[0].split(":")[0].trim();

            if (!scratchcards[card]) { scratchcards[card] = 0; }

            const winners: string[] = allValues[0].split(":")[1].trim().split(" ");
            const myNumbers: string[] = allValues[1].trim().split(" ");

            let count: number = 0;
            myNumbers.forEach((number: string) => {
                if (winners.includes(number) && number !== '') { count++; }
            })

            let repeat: number = scratchcards[card];
            if (count) { repeat++; }

            for (let i = 0; i < repeat; i++) {
                for (let winCard: number = 1; winCard <= count; winCard++) {
                    const numCard: string = (idxRow + winCard + 1).toString().padStart(3, ' ');
                    const key: string = `${card.slice(0, 4)} ${numCard}`;
                    if (!scratchcards[key]) { scratchcards[key] = 1; }
                    else { scratchcards[key] += 1; }
                }
            }

            scratchcards[card] += 1 ;

            if (count - 1 >= 0) {
                let point = 2 ** (count - 1);
                totalPoints += point;
            }
        })

        const totalScratchcards: number[] = Object.values(scratchcards)
            const sumScratchcards = totalScratchcards.reduce((a, b) => a + b, 0)
        return [totalPoints, sumScratchcards]
    } catch (error) {
        return `Error: ${error.message}`;
    }
}


// const result: [number, number]|string = solveDay04();
// console.log("Total Points: ", result[0], "\nTotal Scratchcards: ", result[1])


/*
 * Solution for Advent of Code 2023, Day 06
 * https://adventofcode.com/2023/day/06
 */

import * as fs from "fs";

function solveDay06(filename: string ="./input.txt"): string {
    try {
        const data: string = fs.readFileSync(filename, 'utf8');
        const races: number[][] = data
            .split("\n")
            .map((value: string) => {
                const numbersInLine: string[] = value
                    .split(":")[1]
                    .trim()
                    .split(" ");
                return numbersInLine
                    .filter((v: string):boolean => v.length !== 0)
                    .map((v: string) => parseInt(v))
                    .filter((v: number) => !isNaN(v));
            });
        const records: number[] = [];
        const numRaces: number = races[0].length;
        for (let race: number = 0; race < numRaces; race++) {
            const tMax: number = races[0][race];
            const dRecord: number = races[1][race];
            let recordRace: number = 0;
            for (let vStart: number = 0; vStart <= tMax; vStart++) {
                const distance: number = (tMax - vStart) * vStart;
                if (distance > dRecord) { recordRace ++; }
            }
            if (recordRace) { records.push(recordRace); }
        }

        const numRecords: number = records.reduce((a: number, b: number) => a * b, 1);
        return numRecords.toString();

    } catch (error) { return `Error: ${error.message}`; }
}

// const result: string = solveDay06();
// console.log("Num Records:", result);
// 288
// 633080


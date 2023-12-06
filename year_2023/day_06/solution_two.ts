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

        const tMax: number = parseInt(races[0].join(""));
        const dRecord: number = parseInt(races[1].join(""));
        let numRecords: number = 0;

        for (let vStart: number = 0; vStart <= tMax; vStart++) {
            const distance: number = (tMax - vStart) * vStart;
            if (distance > dRecord)  { numRecords ++; }
        }

        return (numRecords).toString();

    } catch (error) { return `Error: ${error.message}`; }
}

// const result: string = solveDay06();
// console.log("Num Records:", result);
// 71503
// 20048741

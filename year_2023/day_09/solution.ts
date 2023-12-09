/*
 * Solution for Advent of Code 2023, Day 09
 * https://adventofcode.com/2023/day/09
 */

import * as fs from "fs";

function getNextValueHistory(history: number[]): number {
    if (history.every(element => element === 0)) { return 0; }
    const differences: number[] = [];
    for (let i:number = 0; i < history.length - 1; i++) {
        differences.push(history[i + 1] - history[i]);
    }
    return history[history.length-1] + getNextValueHistory(differences);
}


function solveDay09(filename: string ="./input.txt"): [string, string] | string {
    try {
        const data: string = fs.readFileSync(filename, 'utf8');
        const histories: number[][] = data.split('\n')
            .map(history => history.split(' ').map(Number));

        const sumOne: number = histories.map((history: number[]) => {
            return getNextValueHistory(history);
        }).reduce((a: number, b: number) => a + b, 0);

        const sumTwo: number = histories.map((history: number[]) => {
            return getNextValueHistory(history.reverse())
        }).reduce((a: number, b: number) => a + b, 0);

        return [sumOne.toString(), sumTwo.toString()];

    } catch (error) { return `Error: ${error.message}`; }
}

// const sum: [string,string] | string = solveDay09();
// console.log("Sum Part One:", sum[0]);
// console.log("Sum Part Two:", sum[1]);
// // 114
// 2
// 1806615041
// 1211
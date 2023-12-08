/*
 * Solution for Advent of Code 2023, Day 08 - Part 2
 * https://adventofcode.com/2023/day/08
 */

import * as fs from "fs";

function solveDay08(filename: string ="./input_two.txt"): string {
    try {
        const data: string = fs.readFileSync(filename, 'utf8');
        const sequence: string = data.split("\n")[0];
        const lines: string[] = data.split('\n').slice(2);

        const maps: {[key: string]: [string, string]} = {};
        const pathsStart: string[] = [];
        const steps :number[]  = [];

        lines.forEach((line: string): void => {
            const key: string = line.split(" = (")[0];
            if (key[2] === "A") { pathsStart.push(key); }

            const value : string = line.split(" = (")[1];
            const left: string = value.slice(0,3);
            const right: string = value.slice(5, 8);
            maps[key] = [left, right];
        })

        pathsStart.forEach((start: string): void => {
            let stopFounded: boolean = false;
            let key : string = start;
            let step: number = 0;

            while (!stopFounded) {
                for (const direction of sequence) {
                    step++;

                    if (direction === "L") { key = maps[key][0]; }
                    else { key = maps[key][1]; }

                    if (key[2] === "Z") {
                        stopFounded = true;
                        steps.push(step);
                        break;
                    }
                }
            }
        });

        let allStepsSync: number = steps[0];
        for (let i: number = 1; i < steps.length; i++) {
            let currentNumber: number = steps[i];
            let mcd: number = 1;
            let minValue: number = Math.min(allStepsSync, currentNumber);

            for (let j: number = 2; j <= minValue; j++) {
                if (allStepsSync % j === 0 && currentNumber % j === 0) {
                    mcd = j;
                }
            }

            allStepsSync = (allStepsSync * currentNumber) / mcd;
        }

        return allStepsSync.toString();

    } catch (error) { return `Error: ${error.message}`; }
}

// const steps: string = solveDay08();
// console.log("Num Steps:", steps);
// 6
// 11795205644011
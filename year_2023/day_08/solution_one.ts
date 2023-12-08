/*
 * Solution for Advent of Code 2023, Day 08 - Part 1
 * https://adventofcode.com/2023/day/08
 */

import * as fs from "fs";

function solveDay08(filename: string ="./input_one.txt"): string {
    try {
        const data: string = fs.readFileSync(filename, 'utf8');
        const sequence:string = data.split("\n")[0];
        const maps: {[key: string]: [string,string]} = {};
        const start: string = "AAA";
        const stop: string = "ZZZ";
        const lines: string[] = data.split('\n').slice(2);

        lines.forEach((line: string): void => {
            const key: string = line.split(" = (")[0];
            const value: string = line.split(" = (")[1];
            const left: string = value.slice(0,3);
            const right: string = value.slice(5, 8);
            maps[key] = [left, right];
        })

        let stopFounded: boolean = false;
        let step: number = 0;
        let key: string = start;
        while(!stopFounded) {
            for (const directions of sequence) {
                step++;

                if (directions === "L") { key = maps[key][0]; }
                else { key = maps[key][1]; }

                if (key === stop) {
                    stopFounded = true;
                    break;
                }
            }
        }

        return step.toString();

    } catch (error) { return `Error: ${error.message}`; }
}


// const steps: string = solveDay08();
// console.log("Num Steps:", steps);
// 6
// 16409


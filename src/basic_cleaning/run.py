#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import os
import argparse
import logging
import wandb
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    artifact = run.use_artifact(args.input_artifact)
    artifact_path = artifact.file()

    logger.info("INFO: READING INPUT ARTIFACT")
    df = pd.read_csv(artifact_path)

    logger.info("INFO: DROPPING OUTLIERS")
    mask = (df["price"]>=args.min_price) & (df["price"]<=args.max_price) 
    df = df[mask]

    logger.info("INFO: APPLYING DATE FORMAT TO LAST_REVIEW TABLE")
    df["last_review"] = pd.to_datetime(df["last_review"])
    
    logger.info("INFO: SAVING CSV")
    filename = args.output_artifact
    df.to_csv(filename, index=False)

    artifact = wandb.Artifact(
        name = args.output_artifact,
        type = args.output_type,
        description = args.output_description
    )

    artifact.add_file(filename)

    run.log_artifact(artifact)
    logger.info("INFO: ARTIFACT SAVED")

    os.remove(filename)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type = str,
        help = "Name of the input artifact to retrieve from W&B", 
        required = True
    )

    parser.add_argument(
        "--output_artifact", 
        type = str,
        help = "Name for the output artifact to be store in W&B",
        required = True
    )

    parser.add_argument(
        "--output_type", 
        type = str,
        help = "Type for the output artifact",
        required = True
    )

    parser.add_argument(
        "--output_description", 
        type = str,
        help = "Descripton for the output artifact",
        required = True
    )

    parser.add_argument(
        "--min_price", 
        type = float,
        help = "Minimum value accepted for the target variable",
        required = True
    )

    parser.add_argument(
        "--max_price", 
        type = float,
        help = "Maximum value accepted for the target variable",
        required = True
    )


    args = parser.parse_args()

    go(args)

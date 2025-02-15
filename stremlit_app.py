import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useRouter } from "next/router";

export default function DogBoarding() {
  const [form, setForm] = useState({ name: "", date: "", duration: "" });
  const [submitted, setSubmitted] = useState(false);
  const router = useRouter();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
    setTimeout(() => router.push("/confirmation"), 2000);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-4 bg-gray-100">
      <Card className="w-full max-w-md bg-white p-6 rounded-lg shadow-lg">
        <CardContent>
          <h2 className="text-2xl font-bold mb-4">Book Dog Boarding</h2>
          {submitted ? (
            <p className="text-green-600">Booking confirmed! Redirecting...</p>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <Label htmlFor="name">Dog's Name</Label>
                <Input
                  type="text"
                  id="name"
                  name="name"
                  value={form.name}
                  onChange={handleChange}
                  required
                />
              </div>
              <div>
                <Label htmlFor="date">Start Date</Label>
                <Input
                  type="date"
                  id="date"
                  name="date"
                  value={form.date}
                  onChange={handleChange}
                  required
                />
              </div>
              <div>
                <Label htmlFor="duration">Duration (days)</Label>
                <Input
                  type="number"
                  id="duration"
                  name="duration"
                  value={form.duration}
                  onChange={handleChange}
                  required
                />
              </div>
              <Button type="submit" className="w-full bg-blue-500 hover:bg-blue-600">
                Book Now
              </Button>
            </form>
          )}
        </CardContent>
      </Card>
    </div>
  );
}

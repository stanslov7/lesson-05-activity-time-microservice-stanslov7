# lesson-05-activity-time-microservice-stanslov7

You Do: A Simple Time Server
Now, I'd like you to complete a miniature assignment. I'd like for you to create a microservice that provides the current Unix time or epoch time. If you're not familiar with epoch time, you can see the current epoch time here.

Create your microservice in Flask and deploy it to Heroku. When you're done you should be able to visit http://myapp.herokuapp.com/ (for example), and the resulting page will display something like: 1525201581.

You don't have to "turn anything in", but you're going to use this microservice in lesson 10 when you program your microcontrollers. Unlike your computer, your microcontroller doesn't have a battery-driven clock to help it keep track of the time and date when it's unplugged. You'll be programming your microcontroller to reach out to this microservice to find the time and date when it boots up.

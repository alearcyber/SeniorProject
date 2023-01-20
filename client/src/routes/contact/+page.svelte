<script>
    import { Label, Input, Textarea, Button, Card, Heading, List, DescriptionList } from 'flowbite-svelte'

    let commentarea = {
        id: 'message',
        name: 'message',
        label: 'Your message',
        rows: 4,
        placeholder: 'Leave a comment...',
    }
</script>

<div class="space-y-10">
    <div class="text-center">
        <Heading tag="h1" class="mb-4" customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">Get in touch</Heading>
    </div>

    <div class="flex justify-around space-x-10 max-w-5xl m-auto">
        <div class="grow">
            <Card img="../../contact-us.webp">
                <h3 class="mb-2 text-3xl font-bold tracking-tight text-gray-900 dark:text-white">Contact Us</h3>
                <List tag="dl" color="text-gray-900 dark:text-white">
                    <div class="flex flex-col pb-3">
                        <DescriptionList tag="dt" class="mb-1">Email address</DescriptionList>
                        <DescriptionList tag="dd">huntsvilleciviccenter@gmail.com</DescriptionList>
                    </div>
                    <div class="flex flex-col pb-3">
                        <DescriptionList tag="dt" class="mb-1">Phone number</DescriptionList>
                        <DescriptionList tag="dd">(555) 555 - 5555</DescriptionList>
                    </div>
                    <div class="flex flex-col pb-3">
                        <DescriptionList tag="dt" class="mb-1">Home address</DescriptionList>
                        <DescriptionList tag="dd">700 Monroe Street Huntsville, Alabama 35801</DescriptionList>
                    </div>
                </List>
            </Card>
        </div>
        <div class="grow-0">
            <Card>
                <form class="flex flex-col space-y-6" action="/">
                    <h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Leave a comment</h3>
                    <Label class="space-y-2">
                        <span>First Name</span>
                        <Input type="text" name="first-name" placeholder="First Name" required />
                    </Label>
                    <Label class="space-y-2">
                        <span>Last Name</span>
                        <Input type="text" name="last-name" placeholder="Last Name" required />
                    </Label>
                    <Label class="space-y-2">
                        <span>Email</span>
                        <Input type="email" name="email" placeholder="name@company.com" required />
                    </Label>
                    <Label class="space-y-2">
                        <span>Comment</span>
                        <Textarea {...commentarea} required />
                    </Label>
                    <Button type="submit" class="w-full" on:click>Submit</Button>
                </form>
            </Card>
        </div>
    </div>
</div>
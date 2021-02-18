// package com.codility;

// you can also use imports, for example:
// import java.util.*;
// Write a function to insert a node into a linked list
// 
public class interview {

    Node head = null;

    public static void main(String [] args) {
        // you can write to stdout for debugging purposes, e.g.
        
        System.out.println("This is a debug message");
    }

    class Node
    {
        int data;
        Node next = null;
        
        Node(int data)
        {
            this.data = data;
        }
    }
    // can you hear me?
    // I can hear and see you but my microphone is not working??
// I do but I think its a problem with the s

    void insertNodeAtHead(int data)
    {
        
        Node newNode = new Node(data);
        // Make next of the new node the head of the list
        newNode.next = head;
        // Move the head to point to the new Node
        head = newNode;

    }
}

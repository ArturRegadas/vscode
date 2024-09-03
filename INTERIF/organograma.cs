using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string nad = Console.ReadLine();

        Dictionary<string, List<string>> graph = new Dictionary<string, List<string>>();

        while (true)
        {
            string[] edge = Console.ReadLine().Split(' ');
            if (edge[0] == "fim" && edge[1] == "entrada")
            {
                break;
            }
            if (!graph.ContainsKey(edge[1]))
            {
                graph[edge[1]] = new List<string>();
            }
            graph[edge[1]].Add(edge[0]);
        }

        string start = Console.ReadLine();


        List<string> fila = new List<string> { start };
        List<string> processados = new List<string>();


        while (fila.Count > 0)
        {
            string current = fila[0];
            if (graph.ContainsKey(current))
            {
                List<string> paordenar = new List<string>();
                foreach (string i in graph[current])
                {
                    if (!processados.Contains(i))
                    {
                        paordenar.Add(i);
                    }
                }

                paordenar.Sort();
                paordenar.Reverse();


                foreach (string i in paordenar)
                {
                    fila.Insert(1, i);
                }
            }

            Console.WriteLine(current);

            processados.Add(current);
            fila.RemoveAt(0);
        }
    }
}

#!/bin/bash

echo "              ....."
echo "          _d^^^^^^^^^b_"
echo "       .p.             .q."
echo "     .d.      CENTRAL    .b."
echo "    .p.                   .q."
echo "   .d.       @@    @@@@    .b."
echo "  .p.        @@  @@         .q."
echo "   ::        @@  @@         ::"
echo "  ::         @@  @@          ::"
echo "   ::    @@  @@  @@         ::"
echo "   .p.   @@  @@  @@        .q."
echo "    .p.    @@      @@@@   .q."
echo "     .b.                 .d."
echo "       .q.             .p."
echo "          ^q.........p^"
echo "              ''''"


PS3='Escolha uma das opções: '
options=("Ativar a Central" "Sair")
select opt in "${options[@]}"
do
    case $opt in
        "Ativar a Central")
            cd /home/jainaldo/projects/develop/centraljc
            source /home/jainaldo/.virtualenvs/jc/bin/activate
            exec python manage.py runserver 0.0.0.0:8000
            ;;
        "Sair")
            break
            ;;
        *) echo Opção invalida;;
    esac
done
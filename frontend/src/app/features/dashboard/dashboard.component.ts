import { ChangeDetectionStrategy, Component, computed, signal } from "@angular/core";

interface ComplianceItem {
  name: string;
  status: "urgent" | "in-progress" | "validated";
  lastUpdate: string;
}

@Component({
  selector: "tej-dashboard",
  standalone: true,
  templateUrl: "./dashboard.component.html",
  styleUrl: "./dashboard.component.css",
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DashboardComponent {
  private readonly items = signal<ComplianceItem[]>([
    {
      name: "Société Alpha",
      status: "urgent",
      lastUpdate: "Retenues du mois à générer",
    },
    {
      name: "Clinique Beta",
      status: "in-progress",
      lastUpdate: "Fichiers importés, validation en cours",
    },
    {
      name: "Garage Gamma",
      status: "validated",
      lastUpdate: "XML généré et déposé",
    },
  ]);

  readonly urgentCount = computed(
    () => this.items().filter((item) => item.status === "urgent").length,
  );
  readonly inProgressCount = computed(
    () => this.items().filter((item) => item.status === "in-progress").length,
  );
  readonly validatedCount = computed(
    () => this.items().filter((item) => item.status === "validated").length,
  );
  readonly complianceItems = computed(() => this.items());

  readonly activityHighlights = signal([
    {
      title: "Certificats traités",
      value: "150",
      helper: "Ce mois-ci",
    },
    {
      title: "Montant total RS",
      value: "38,2k TND",
      helper: "Sur 12 dossiers",
    },
    {
      title: "Temps gagné",
      value: "42h",
      helper: "Automatisation Nexus",
    },
  ]);
}

%global packname  seqDesign
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          Simulation and Group Sequential Monitoring of RandomizedTwo-Stage Treatment Efficacy Trials with Time-to-EventEndpoints

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.16
Requires:         R-core >= 2.16
BuildArch:        noarch
BuildRequires:    R-survival 
Requires:         R-survival 

%description
A modification of the preventive vaccine efficacy trial design of Gilbert,
Grove et al. (2011, Statistical Communications in Infectious Diseases) is
implemented, with application generally to individual-randomized clinical
trials with multiple active treatment groups and a shared control group,
and a study endpoint that is a time-to-event endpoint subject to
right-censoring. The design accounts for the issues that the efficacy of
the treatment/vaccine groups may take time to accrue while the multiple
treatment administrations/vaccinations are given; there is interest in
assessing the durability of treatment efficacy over time; and group
sequential monitoring of each treatment group for potential harm,
non-efficacy/efficacy futility, and high efficacy is warranted. The design
divides the trial into two stages of time periods, where each treatment is
first evaluated for efficacy in the first stage of follow-up, and, if and
only if it shows significant treatment efficacy in stage one, it is
evaluated for longer-term durability of efficacy in stage two. The package
produces plots and tables describing operating characteristics of a
specified design including an unconditional power for intention-to-treat
and per-protocol/as-treated analyses; trial duration; probabilities of the
different possible trial monitoring outcomes (e.g., stopping early for
non-efficacy); unconditional power for comparing treatment efficacies; and
distributions of numbers of endpoint events occurring after the
treatments/vaccinations are given, useful as input parameters for the
design of studies of the association of biomarkers with a clinical outcome
(surrogate endpoint problem). The code can be used for a single active
treatment versus control design and for a single-stage design.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

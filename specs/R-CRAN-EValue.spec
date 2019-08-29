%global packname  EValue
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Sensitivity Analyses for Unmeasured Confounding or SelectionBias in Observational Studies and Meta-Analyses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-devtools 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-devtools 

%description
Conducts sensitivity analyses for unmeasured confounding for either an
observational study or a meta-analysis of observational studies. For a
single observational study, the package reports E-values, defined as the
minimum strength of association on the risk ratio scale that an unmeasured
confounder would need to have with both the treatment and the outcome to
fully explain away a specific treatment-outcome association, conditional
on the measured covariates. You can use one of the evalues.XX() functions
to compute E-values for the relevant outcome types. Outcome types include
risk ratios, odds ratio with common or rare outcomes, hazard ratios with
common or rare outcomes, and standardized differences in outcomes.
Optionally, you can use the bias_plot() function to plot the bias factor
as a function of two sensitivity parameters. (See VanderWeele & Ding, 2017
[<http://annals.org/aim/article/2643434>] for details.) For a
meta-analysis, use the function confounded_meta to compute point estimates
and inference for: (1) the proportion of studies with true causal effect
sizes more extreme than a specified threshold of scientific importance;
and (2) the minimum bias factor and confounding strength required to
reduce to less than a specified threshold the proportion of studies with
true effect sizes of scientifically significant size. The functions
sens_plot() and sens_table() create plots and tables for visualizing these
meta-analysis metrics across a range of bias values. (See Mathur &
VanderWeele, 2019
[<https://amstat.tandfonline.com/doi/full/10.1080/01621459.2018.1529598#.XKIJtOtKjdc>]
for details.) Most of the analyses available in this package can also be
conducted using web-based graphical interfaces (for a single observational
study: [<https://evalue.hmdc.harvard.edu>]; for a meta-analysis:
[<https://mmathur.shinyapps.io/meta_gui_2/>]).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX

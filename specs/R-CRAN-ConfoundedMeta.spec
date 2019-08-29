%global packname  ConfoundedMeta
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          Sensitivity Analyses for Unmeasured Confounding in Meta-Analyses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-metafor 
Requires:         R-stats 

%description
Conducts sensitivity analyses for unmeasured confounding in random-effects
meta-analysis per Mathur & VanderWeele (in preparation). Given output from
a random-effects meta-analysis with a relative risk outcome, computes
point estimates and inference for: (1) the proportion of studies with true
causal effect sizes more extreme than a specified threshold of scientific
significance; and (2) the minimum bias factor and confounding strength
required to reduce to less than a specified threshold the proportion of
studies with true effect sizes of scientifically significant size. Creates
plots and tables for visualizing these metrics across a range of bias
values. Provides tools to easily scrape study-level data from a published
forest plot or summary table to obtain the needed estimates when these are
not reported.

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
%{rlibdir}/%{packname}/INDEX

%global packname  odr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Optimal Design and Statistical Power of Multilevel RandomizedTrials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.0.0
BuildRequires:    R-graphics >= 3.0.0
BuildRequires:    R-base >= 3.0.0
Requires:         R-stats >= 3.0.0
Requires:         R-graphics >= 3.0.0
Requires:         R-base >= 3.0.0

%description
Calculate the optimal sample allocation that minimizes the variance of
treatment effect in multilevel randomized trials under fixed budget and
cost structure, perform power analyses with and without accommodating
costs and budget. The references for proposed methods are: (1) Shen, Z.
(in progress). Using optimal sample allocation to improve statistical
precision and design efficiency for multilevel randomized trials.
(unpublished doctoral dissertation). University of Cincinnati, Cincinnati,
OH. (2) Shen, Z., & Kelcey, B. (revise & resubmit). Optimal sample
allocation accounts for the full variation of sampling costs in
cluster-randomized trials. Journal of Educational and Behavioral
Statistics. (3) Shen, Z., & Kelcey, B. (2018, April). Optimal design of
cluster randomized trials under condition- and unit-specific cost
structures. Roundtable discussion presented at American Educational
Research Association (AERA) annual conference. (4) Champely., S. (2018).
pwr: Basic functions for power analysis (Version 1.2-2) [Software].
Available from <https://CRAN.R-project.org/package=pwr>.

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
%doc %{rlibdir}/%{packname}/NEWS.Rmd
%{rlibdir}/%{packname}/INDEX

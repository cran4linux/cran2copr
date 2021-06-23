%global __brp_check_rpaths %{nil}
%global packname  odr
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
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
Calculate the optimal sample allocation that produces smallest variance of
a treatment effect or the highest statistical power for experimental
studies under a budget constraint, perform power analyses with and without
accommodating cost structures of sampling, and calculate the relative
efficiency between two sample allocations. The references for the proposed
methods are: (1) Shen, Z. (2019). Optimal sample allocation in multilevel
Experiments. (Doctoral dissertation). University of Cincinnati,
Cincinnati, OH. (2) Shen, Z., & Kelcey, B. (in press). Optimal sample
allocation under unequal costs in cluster-randomized trials. Journal of
Educational and Behavioral Statistics. (3) Champely., S. (2018). pwr:
Basic functions for power analysis (Version 1.2-2) [Software]. Available
from <https://CRAN.R-project.org/package=pwr>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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

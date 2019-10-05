%global packname  HACSim
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Iterative Extrapolation of Species' Haplotype AccumulationCurves

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape >= 5.2
BuildRequires:    R-graphics >= 3.5.1
BuildRequires:    R-stats >= 3.5.1
BuildRequires:    R-utils >= 3.5.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-pegas >= 0.11
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ape >= 5.2
Requires:         R-graphics >= 3.5.1
Requires:         R-stats >= 3.5.1
Requires:         R-utils >= 3.5.1
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-pegas >= 0.11

%description
Performs iterative extrapolation of species' haplotype accumulation curves
using a nonparametric stochastic (Monte Carlo) optimization method for
assessment of specimen sampling completeness based on the approach of
Phillips et al. (2015) <doi:10.1515/dna-2015-0008> and Phillips et al.
(2019) <doi:10.1002/ece3.4757>. Any genomic marker can be targeted to
assess likely required specimen sample sizes. The method is well-suited to
assess sampling sufficiency for DNA barcoding initiatives.

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
%{rlibdir}/%{packname}/libs

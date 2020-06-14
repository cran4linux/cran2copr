%global packname  gppm
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Gaussian Process Panel Modeling

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.49
BuildRequires:    R-CRAN-ggthemes >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-rstan >= 2.17.3
BuildRequires:    R-CRAN-mvtnorm >= 1.0.8
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-MASS >= 7.3.49
Requires:         R-CRAN-ggthemes >= 3.5.0
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-rstan >= 2.17.3
Requires:         R-CRAN-mvtnorm >= 1.0.8
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-stats 
Requires:         R-methods 

%description
Provides an implementation of Gaussian process panel modeling (GPPM). GPPM
is described in Karch (2016; <DOI:10.18452/17641>) and Karch, Brandmaier &
Voelkle (2018; <DOI:10.17605/OSF.IO/KVW5Y>). Essentially, GPPM is Gaussian
process based modeling of longitudinal panel data. 'gppm' also supports
regular Gaussian process regression (with a focus on flexible model
specification), and multi-task learning.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/demo_helpers.R
%doc %{rlibdir}/%{packname}/stanTemplate.stan
%{rlibdir}/%{packname}/INDEX

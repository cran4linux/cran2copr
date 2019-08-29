%global packname  cooccur
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Probabilistic Species Co-Occurrence Analysis in R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-ggplot2 

%description
This R package applies the probabilistic model of species co-occurrence
(Veech 2013) to a set of species distributed among a set of survey or
sampling sites. The algorithm calculates the observed and expected
frequencies of co-occurrence between each pair of species. The expected
frequency is based on the distribution of each species being random and
independent of the other species. The analysis returns the probabilities
that a more extreme (either low or high) value of co-occurrence could have
been obtained by chance. The package also includes functions for
visualizing species co-occurrence results and preparing data for
downstream analyses.

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

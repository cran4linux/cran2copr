%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DEploid.utils
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          'DEploid' Data Analysis and Results Interpretation

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-scales >= 0.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-combinat 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-scales >= 0.4.0
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-combinat 

%description
'DEploid' (Zhu et.al. 2018 <doi:10.1093/bioinformatics/btx530>) is
designed for deconvoluting mixed genomes with unknown proportions.
Traditional phasing programs are limited to diploid organisms. Our method
modifies Li and Stephen’s algorithm with Markov chain Monte Carlo (MCMC)
approaches, and builds a generic framework that allows haloptype searches
in a multiple infection setting. This package provides R functions to
support data analysis and results interpretation.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

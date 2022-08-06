%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metaMix
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Mixture Analysis for Metagenomic Community Profiling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-data.table >= 1.9.2
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-Rmpi 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-data.table >= 1.9.2
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-Rmpi 
Requires:         R-CRAN-ggplot2 

%description
Resolves complex metagenomic mixtures by analysing deep sequencing data,
using a mixture model based approach. The use of parallel Monte Carlo
Markov chains for the exploration of the species space enables the
identification of the set of species more likely to contribute to the
mixture.

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

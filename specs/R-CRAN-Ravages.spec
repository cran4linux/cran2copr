%global __brp_check_rpaths %{nil}
%global packname  Ravages
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rare Variant Analysis and Genetic Simulations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-mlogit >= 1.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gaston 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-dfidx 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-bedr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-mlogit >= 1.1.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-methods 
Requires:         R-CRAN-gaston 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-dfidx 
Requires:         R-parallel 
Requires:         R-CRAN-bedr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 

%description
Rare variant association tests: burden tests (Bocher et al. 2019
<doi:10.1002/gepi.22210>) and the Sequence Kernel Association Test (Bocher
et al. 2021 <doi:10.1038/s41431-020-00792-8>) in the whole genome; and
genetic simulations.

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

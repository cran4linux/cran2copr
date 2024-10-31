%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FuzzyImputationTest
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Imputation Procedures and Quality Tests for Fuzzy Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-FuzzySimRes 
BuildRequires:    R-CRAN-FuzzyNumbers 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-miceRanger 
BuildRequires:    R-CRAN-VIM 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-FuzzySimRes 
Requires:         R-CRAN-FuzzyNumbers 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-miceRanger 
Requires:         R-CRAN-VIM 
Requires:         R-utils 

%description
Special procedures for the imputation of missing fuzzy numbers are still
underdeveloped. The goal of the package is to provide the new d-imputation
method (DIMP for short, Romaniuk, M. and Grzegorzewski, P. (2023) "Fuzzy
Data Imputation with DIMP and FGAIN" RB/23/2023) and covert some classical
ones applied in R packages ('missForest','miceRanger','knn') for use with
fuzzy datasets. Additionally, specially tailored benchmarking tests are
provided to check and compare these imputation procedures with fuzzy
datasets.

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

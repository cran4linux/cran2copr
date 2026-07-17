%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BIGpopA
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Pedigree Validation Genetic Composition of Diploids & Polyploids

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 

%description
Tools for pedigree quality control and genomic breed/line composition
estimation in diploid and polyploid breeding populations. 'BIGpopA'
provides functions to check and correct common pedigree errors, assign
parentage from SNP genotype data using Mendelian error rates, validate
parent-offspring trios, and estimate genome-wide breed or line composition
using quadratic programming. Supports both diploid and polyploid species.
For more details about the included 'breedTools' functions, see Funkhouser
et al. (2017) <doi:10.2527/tas2016.0003>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  migest
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Estimating, Measuring and Working with Migration Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-migration.indices 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-mipfp 
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-forcats 
Requires:         R-utils 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-migration.indices 
Requires:         R-CRAN-circlize 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-mipfp 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-lpSolve 

%description
Provides tools for estimating, measuring, and analyzing migration data.
Designed to assist researchers and analysts in working effectively with
migration data.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gasanalyzer
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Import, Recompute and Analyze Data from Portable Gas Analyzers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyxl >= 1.0.8
BuildRequires:    R-CRAN-jsonify 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-tidyxl >= 1.0.8
Requires:         R-CRAN-jsonify 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-CRAN-units 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-xml2 

%description
Provides functions to import data from several instruments commonly used
by plant physiologists to measure characteristics related to
photosynthesis. It provides a standardized list of variable names, and
several sets of equations to calculate additional variables based on the
measurements.  These equations have been described by von Caemmerer and
Farquhar (1981) <doi:10.1007/BF00384257>, Busch et al. (2020)
<doi:10.1038/s41477-020-0606-6> and Márquez et al. (2021)
<doi:10.1038/s41477-021-00861-w>. In addition, this package facilitates
performing sensitivity analyses on variables or assumptions used in the
calculations.

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

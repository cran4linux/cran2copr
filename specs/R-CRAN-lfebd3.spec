%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lfebd3
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generation and Analysis of 3-Level and 5-Level Factorial Block Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides tools to generate and analyze 3-level and 5-level linear
factorial block designs, including complete factorial layouts, fractional
factorial layouts, confounded factorial layouts, and design-characteristic
summaries. The package includes utilities for recursive construction,
defining-contrast identification, alias and confounding summaries,
incidence matrix construction, and selected design-characteristic
diagnostics. The methodological framework follows foundational work on
factorial block designs, including Gupta (1983)
<doi:10.1111/j.2517-6161.1983.tb01253.x>.

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

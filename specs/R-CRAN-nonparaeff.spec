%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nonparaeff
%global packver   0.5-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.15
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Methods for Measuring Efficiency and Productivity

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-lpSolve 

%description
Efficiency and productivity indices are measured using this package. This
package contains functions for measuring efficiency and productivity of
decision making units (DMUs) under the framework of Data Envelopment
Analysis (DEA) and its variations.

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

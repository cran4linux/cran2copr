%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wildlifeDI
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Indices of Dynamic Interaction for Wildlife Tracking Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-move2 
BuildRequires:    R-CRAN-adehabitatLT 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-lwgeom 
Requires:         R-CRAN-move2 
Requires:         R-CRAN-adehabitatLT 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-units 
Requires:         R-CRAN-lwgeom 

%description
Dynamic interaction refers to spatial-temporal associations in the
movements of two (or more) animals. This package provides tools for
calculating a suite of indices used for quantifying dynamic interaction
with wildlife telemetry data. For more information on each of the methods
employed see the references within. The package (as of version >= 0.3)
also has new tools for automating contact analysis in large tracking
datasets. The package (as of version 1.0) uses the 'move2' class of
objects for working with tracking dataset.

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

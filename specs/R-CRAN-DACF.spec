%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DACF
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Analysis with Ceiling and/or Floor Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-psych 
Requires:         R-utils 

%description
An implementation of data analytic methods in R for analyses for data with
ceiling/floor effects. The package currently includes functions for
mean/variance estimation and mean comparison tests. Implemented methods
are from Aitkin (1964) <doi:10.1007/BF02289723> and Liu & Wang (2021)
<doi:10.3758/s13428-020-01407-2>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NMsim
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Seamless 'Nonmem' Simulation Platform

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-NMdata >= 0.2.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-CRAN-xfun 
Requires:         R-CRAN-NMdata >= 0.2.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-fst 
Requires:         R-CRAN-xfun 

%description
A complete and seamless 'Nonmem' simulation interface within R. Turns
'Nonmem' control streams into simulation control streams, executes them
with specified simulation input data and returns the results. The
simulation is performed by 'Nonmem', eliminating manual work and risks of
re-implementation of models in other tools.

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

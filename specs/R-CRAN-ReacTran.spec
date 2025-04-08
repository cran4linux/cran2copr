%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ReacTran
%global packver   1.4.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Reactive Transport Modelling in 1d, 2d and 3d

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-shape 
Requires:         R-stats 
Requires:         R-graphics 

%description
Routines for developing models that describe reaction and
advective-diffusive transport in one, two or three dimensions. Includes
transport routines in porous media, in estuaries, and in bodies with
variable shape.

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

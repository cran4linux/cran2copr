%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geospt
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Geostatistical Analysis and Design of Optimal Spatial Sampling Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-genalg 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-sgeostat 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-genalg 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-sgeostat 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-utils 

%description
Estimation of the variogram through trimmed mean, radial basis functions
(optimization, prediction and cross-validation), summary statistics from
cross-validation, pocket plot, and design of optimal sampling networks
through sequential and simultaneous points methods.

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

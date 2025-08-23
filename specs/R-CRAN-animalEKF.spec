%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  animalEKF
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Extended Kalman Filters for Animal Movement

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-bezier 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-png 
Requires:         R-grDevices 
Requires:         R-CRAN-bezier 
Requires:         R-CRAN-HDInterval 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 

%description
Synthetic generation of 1-D and 2-D correlated random walks (CRWs) for
animal movement with behavioral switching, and particle filter estimation
of movement parameters from observed trajectories using Extended Kalman
Filter (EKF) model. See Ackerman (2018)
<https://digital.library.temple.edu/digital/collection/p245801coll10/id/499150>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sphereclust
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model Based Clustering for Spherical Data Using Elliptically Symmetric Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Directional 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-mixture 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rangen 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
Requires:         R-CRAN-Directional 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-mixture 
Requires:         R-parallel 
Requires:         R-CRAN-rangen 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 

%description
Model based clustering with spherical data using mixtures of elliptically
symmetric distributions, namely mixtures of spherical elliptically
symmetric projected Cauchy (SESPC) or mixtures of elliptically symmetric
angular Gaussian (ESAG) distributions. The relevant paper is: Perdikis T.,
Alharbi N. and Tsagris M. (2026). <doi:10.48550/arXiv.2605.27496>.

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

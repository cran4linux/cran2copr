%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ezECM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Event Categorization Matrix Classification for Nuclear Detonations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-klaR 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mvnfast 
Requires:         R-CRAN-ellipse 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-klaR 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-mvnfast 

%description
Implementation of an Event Categorization Matrix (ECM) detonation
detection model and a Bayesian variant. Functions are provided for
importing and exporting data, fitting models, and applying decision
criteria for categorizing new events. This package implements methods
described in the paper "Bayesian Event Categorization Matrix Approach for
Nuclear Detonations" Koermer, Carmichael, and Williams (2024) available on
arXiv at <doi:10.48550/arXiv.2409.18227>.

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

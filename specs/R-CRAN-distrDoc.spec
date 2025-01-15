%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  distrDoc
%global packver   2.8.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.5
Release:          1%{?dist}%{?buildtag}
Summary:          Documentation for 'distr' Family of R Packages

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-distr >= 2.2.0
BuildRequires:    R-CRAN-distrEx >= 2.2.0
BuildRequires:    R-CRAN-distrSim >= 2.2.0
BuildRequires:    R-CRAN-distrTEst >= 2.2.0
BuildRequires:    R-CRAN-distrTeach >= 2.2.0
BuildRequires:    R-CRAN-distrMod >= 2.2.0
BuildRequires:    R-CRAN-startupmsg >= 1.0.0
BuildRequires:    R-CRAN-RandVar >= 0.7
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-distr >= 2.2.0
Requires:         R-CRAN-distrEx >= 2.2.0
Requires:         R-CRAN-distrSim >= 2.2.0
Requires:         R-CRAN-distrTEst >= 2.2.0
Requires:         R-CRAN-distrTeach >= 2.2.0
Requires:         R-CRAN-distrMod >= 2.2.0
Requires:         R-CRAN-startupmsg >= 1.0.0
Requires:         R-CRAN-RandVar >= 0.7
Requires:         R-CRAN-MASS 
Requires:         R-methods 

%description
Provides documentation in form of a common vignette to packages 'distr',
'distrEx', 'distrMod', 'distrSim', 'distrTEst', 'distrTeach', and
'distrEllipse'.

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

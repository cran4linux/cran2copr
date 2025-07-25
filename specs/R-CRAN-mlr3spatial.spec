%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3spatial
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Support for Spatial Objects Within the 'mlr3' Ecosystem

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-terra >= 1.6.3
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-lgr >= 0.4.2
BuildRequires:    R-CRAN-mlr3 >= 0.14.0
BuildRequires:    R-CRAN-mlr3misc >= 0.11.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-terra >= 1.6.3
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-lgr >= 0.4.2
Requires:         R-CRAN-mlr3 >= 0.14.0
Requires:         R-CRAN-mlr3misc >= 0.11.0
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-utils 

%description
Extends the 'mlr3' ML framework with methods for spatial objects. Data
storage and prediction are supported for packages 'terra', 'raster' and
'stars'.

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

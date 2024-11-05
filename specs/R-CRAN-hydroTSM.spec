%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hydroTSM
%global packver   0.7-0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Management and Analysis for Hydrological Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.7.2
BuildRequires:    R-CRAN-xts >= 0.9.7
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-classInt 
Requires:         R-CRAN-zoo >= 1.7.2
Requires:         R-CRAN-xts >= 0.9.7
Requires:         R-CRAN-e1071 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-classInt 

%description
S3 functions for management, analysis, interpolation and plotting of time
series used in hydrology and related environmental sciences. In
particular, this package is highly oriented to hydrological modelling
tasks. The focus of this package has been put in providing a collection of
tools useful for the daily work of hydrologists (although an effort was
made to optimise each function as much as possible, functionality has had
priority over speed). Bugs / comments / questions / collaboration of any
kind are very welcomed, and in particular, datasets that can be included
in this package for academic purposes.

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

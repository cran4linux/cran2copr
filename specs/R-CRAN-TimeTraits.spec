%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TimeTraits
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Data Analysis Pipeline, Extracting Functional Traits from Biological Time-Series Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-lomb 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-fdaoutlier 
Requires:         R-stats 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-lomb 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-fdaoutlier 

%description
Provides a pipeline of tools for analysing circadian time-series data
using functional data analysis (FDA). The package supports smoothing of
rhythmic time series, functional principle component analysis (FPCA), and
extraction of group-level traits from functional representations. Analyses
can incorporate multiple curve derivatives and optional temporal
segmentation, enabling comparative analysis of circadian dynamics across
experimental groups and time windows.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kernelPhil
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel Smoothing Tools for Philology and Historical Dialectology

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-benchmarkme 
BuildRequires:    R-CRAN-directlabels 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-wordspace 
Requires:         R-CRAN-benchmarkme 
Requires:         R-CRAN-directlabels 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-utils 
Requires:         R-CRAN-wordspace 

%description
Contains kernel smoothing tools designed for use by historical
dialectologists and philologists for exploring spatial and temporal
patterns in noisy historical language data, such as that obtained from
historical texts. The main way in which these might differ from other
implementations of kernel smoothing is that they assume that the function
(linguistic variable) being explored has the form of the relative
frequency of a series of discrete possibilities (linguistic variants).
This package also offers a way of exploring distributions in 2-dimensional
space and in time with separate kernels, and tools for identifying
appropriate bandwidths for these.

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

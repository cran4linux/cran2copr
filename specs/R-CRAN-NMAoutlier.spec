%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NMAoutlier
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Detecting Outliers in Network Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 8.0.1
BuildRequires:    R-CRAN-MASS >= 7.3.47
BuildRequires:    R-stats >= 3.4.3
BuildRequires:    R-parallel >= 3.4.1
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-netmeta >= 0.9.7
Requires:         R-CRAN-meta >= 8.0.1
Requires:         R-CRAN-MASS >= 7.3.47
Requires:         R-stats >= 3.4.3
Requires:         R-parallel >= 3.4.1
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-netmeta >= 0.9.7

%description
A set of functions providing several outlier (i.e., studies with extreme
findings) and influential detection measures and methodologies in network
meta-analysis : - simple outlier and influential detection measures -
outlier and influential detection measures by considering study deletion
(shift the mean) - plots for outlier and influential detection measures -
Q-Q plot for network meta-analysis - Forward Search algorithm in network
meta-analysis. - forward plots to monitor statistics in each step of the
forward search algorithm - forward plots for summary estimates and their
confidence intervals in each step of forward search algorithm.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WebAnalytics
%global packver   0.9.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.12
Release:          1%{?dist}%{?buildtag}
Summary:          Web Server Log Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-xtable >= 1.8.4
BuildRequires:    R-CRAN-fs >= 1.5.2
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-data.table >= 1.14.2
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-brew >= 1.0.6
BuildRequires:    R-CRAN-digest >= 0.6.29
BuildRequires:    R-CRAN-tinytex >= 0.37
BuildRequires:    R-CRAN-uaparserjs >= 0.3.5
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-xtable >= 1.8.4
Requires:         R-CRAN-fs >= 1.5.2
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-data.table >= 1.14.2
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-brew >= 1.0.6
Requires:         R-CRAN-digest >= 0.6.29
Requires:         R-CRAN-tinytex >= 0.37
Requires:         R-CRAN-uaparserjs >= 0.3.5
Requires:         R-utils 

%description
Provides Apache and IIS log analytics for transaction performance, client
populations and workload definitions.

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

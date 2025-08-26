%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gsDesign
%global packver   3.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Group Sequential Design

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-r2rtf 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-graphics 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-r2rtf 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-CRAN-xtable 

%description
Derives group sequential clinical trial designs and describes their
properties. Particular focus on time-to-event, binary, and continuous
outcomes. Largely based on methods described in Jennison, Christopher and
Turnbull, Bruce W., 2000, "Group Sequential Methods with Applications to
Clinical Trials" ISBN: 0-8493-0316-8.

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

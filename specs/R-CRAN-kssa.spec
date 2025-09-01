%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kssa
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Known Sub-Sequence Algorithm

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-imputeTS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-missMethods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-imputeTS 
Requires:         R-stats 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-missMethods 

%description
Implements the Known Sub-Sequence Algorithm
<doi:10.1016/j.aaf.2021.12.013>, which helps to automatically identify and
validate the best method for missing data imputation in a time series.
Supports the comparison of multiple state-of-the-art algorithms.

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

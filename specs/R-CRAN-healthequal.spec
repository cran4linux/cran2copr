%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  healthequal
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Compute Summary Measures of Health Inequality

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-marginaleffects 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-srvyr 
BuildRequires:    R-CRAN-survey 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-marginaleffects 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-srvyr 
Requires:         R-CRAN-survey 

%description
Compute 21 summary measures of health inequality and its corresponding
confidence intervals for ordered and non-ordered dimensions using
disaggregated data. Measures for ordered dimensions (e.g., Slope Index of
Inequality, Absolute Concentration Index) also accept individual and
survey data.

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

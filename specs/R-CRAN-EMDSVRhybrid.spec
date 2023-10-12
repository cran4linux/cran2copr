%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EMDSVRhybrid
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Empirical Mode Decomposition Based Support Vector Regression Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-EMD 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-EMD 
Requires:         R-CRAN-e1071 

%description
Description: Application of empirical mode decomposition based support
vector regression model for nonlinear and non stationary univariate time
series forecasting. For method details see (i) Choudhury (2019)
<http://krishi.icar.gov.in/jspui/handle/123456789/44873>; (ii) Das (2020)
<http://krishi.icar.gov.in/jspui/handle/123456789/43174>; (iii) Das (2023)
<http://krishi.icar.gov.in/jspui/handle/123456789/77772>.

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

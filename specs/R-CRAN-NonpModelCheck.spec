%global __brp_check_rpaths %{nil}
%global packname  NonpModelCheck
%global packver   4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Model Checking and Variable Selection in Nonparametric Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-dr 
Requires:         R-CRAN-dr 

%description
Provides tests of significance for covariates (or groups of covariates) in
a fully nonparametric regression model and a variable (or group) selection
procedure based on False Discovery Rate. In addition, it provides a
function for local polynomial regression for any number of dimensions,
using a bandwidth specified by the user or automatically chosen by cross
validation or an adaptive procedure. Zambom and Akritas (2014)
<doi:10.5705/ss.2013.112>, Zambom and Akritas (2015)
<doi:10.1016/j.jmva.2014.08.014>, Zambom and Akritas (2017)
<doi:10.18637/jss.v077.i10>.

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

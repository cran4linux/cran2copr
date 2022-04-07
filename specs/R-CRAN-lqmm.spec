%global __brp_check_rpaths %{nil}
%global packname  lqmm
%global packver   1.5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.8
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Quantile Mixed Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-nlme >= 3.1.124
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-SparseGrid 
Requires:         R-CRAN-nlme >= 3.1.124
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-SparseGrid 

%description
Functions to fit quantile regression models for hierarchical data (2-level
nested designs) as described in Geraci and Bottai (2014, Statistics and
Computing) <doi:10.1007/s11222-013-9381-9>. A vignette is given in Geraci
(2014, Journal of Statistical Software) <doi:10.18637/jss.v057.i13> and
included in the package documents. The packages also provides functions to
fit quantile models for independent data and for count responses.

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

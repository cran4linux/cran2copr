%global __brp_check_rpaths %{nil}
%global packname  bujar
%global packver   0.2-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Buckley-James Regression for Survival Data with High-Dimensional Covariates

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-CRAN-mpath 
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-elasticnet 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-modeltools 
BuildRequires:    R-CRAN-bst 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-mda 
Requires:         R-CRAN-mpath 
Requires:         R-CRAN-mboost 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-elasticnet 
Requires:         R-CRAN-rms 
Requires:         R-methods 
Requires:         R-CRAN-modeltools 
Requires:         R-CRAN-bst 
Requires:         R-parallel 
Requires:         R-CRAN-survival 

%description
Buckley-James regression for right-censoring survival data with
high-dimensional covariates. Implementations for survival data include
boosting with componentwise linear least squares, componentwise smoothing
splines, regression trees and MARS. Other high-dimensional tools include
penalized regression for survival data. See Wang and Wang (2010)
<doi:10.2202/1544-6115.1550>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

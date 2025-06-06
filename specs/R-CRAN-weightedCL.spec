%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weightedCL
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient and Feasible Inference for High-Dimensional Normal Copula Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-sure 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-sure 
Requires:         R-CRAN-MASS 

%description
Estimates high-dimensional multivariate normal copula regression models
with the weighted composite likelihood estimating equations in
Nikoloulopoulos (2023) <doi:10.1016/j.csda.2022.107654>. It provides
autoregressive moving average correlation structures and binary, ordinal,
Poisson, and negative binomial regressions.

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

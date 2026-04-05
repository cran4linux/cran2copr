%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  poissonsuperlearner
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Poisson Super Learner

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-riskRegression 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lava 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-mgcv 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-riskRegression 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-lava 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-mgcv 

%description
Provides tools for fitting piece-wise constant hazard models for survival
and competing risks data, including ensemble hazard estimation via the
Super Learner framework. The package supports estimation of survival
functions and absolute risk predictions from fitted cause-specific hazard
models. For the Super Learner framework see van der Laan, Polley and
Hubbard (2007) <doi:10.2202/1544-6115.1309>.

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

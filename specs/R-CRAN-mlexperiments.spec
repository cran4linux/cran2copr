%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlexperiments
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Experiments

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-kdry 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-splitTools 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-kdry 
Requires:         R-parallel 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-splitTools 
Requires:         R-stats 

%description
Provides 'R6' objects to perform parallelized hyperparameter optimization
and cross-validation. Hyperparameter optimization can be performed with
Bayesian optimization (via 'ParBayesianOptimization'
<https://cran.r-project.org/package=ParBayesianOptimization>) and grid
search. The optimized hyperparameters can be validated using k-fold
cross-validation. Alternatively, hyperparameter optimization and
validation can be performed with nested cross-validation. While
'mlexperiments' focuses on core wrappers for machine learning experiments,
additional learner algorithms can be supplemented by inheriting from the
provided learner base class.

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

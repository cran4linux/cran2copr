%global __brp_check_rpaths %{nil}
%global packname  mlrMBO
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Optimization and Model-Based Optimization of Expensive Black-Box Functions

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-mlr >= 2.10
BuildRequires:    R-CRAN-checkmate >= 1.8.2
BuildRequires:    R-CRAN-smoof >= 1.5.1
BuildRequires:    R-CRAN-parallelMap >= 1.3
BuildRequires:    R-CRAN-BBmisc >= 1.11
BuildRequires:    R-CRAN-ParamHelpers >= 1.10
BuildRequires:    R-CRAN-backports >= 1.1.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lhs 
Requires:         R-CRAN-mlr >= 2.10
Requires:         R-CRAN-checkmate >= 1.8.2
Requires:         R-CRAN-smoof >= 1.5.1
Requires:         R-CRAN-parallelMap >= 1.3
Requires:         R-CRAN-BBmisc >= 1.11
Requires:         R-CRAN-ParamHelpers >= 1.10
Requires:         R-CRAN-backports >= 1.1.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lhs 

%description
Flexible and comprehensive R toolbox for model-based optimization ('MBO'),
also known as Bayesian optimization. It implements the Efficient Global
Optimization Algorithm and is designed for both single- and multi-
objective optimization with mixed continuous, categorical and conditional
parameters. The machine learning toolbox 'mlr' provide dozens of
regression learners to model the performance of the target algorithm with
respect to the parameter settings. It provides many different infill
criteria to guide the search process. Additional features include
multi-point batch proposal, parallel execution as well as visualization
and sophisticated logging mechanisms, which is especially useful for
teaching and understanding of algorithm behavior. 'mlrMBO' is implemented
in a modular fashion, such that single components can be easily replaced
or adapted by the user for specific use cases.

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

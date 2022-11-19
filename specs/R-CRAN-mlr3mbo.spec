%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3mbo
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Bayesian Optimization

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-bbotk >= 0.5.4
BuildRequires:    R-CRAN-lgr >= 0.3.4
BuildRequires:    R-CRAN-mlr3tuning >= 0.14.0
BuildRequires:    R-CRAN-mlr3 >= 0.14.0
BuildRequires:    R-CRAN-mlr3misc >= 0.11.0
BuildRequires:    R-CRAN-paradox >= 0.10.0
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-bbotk >= 0.5.4
Requires:         R-CRAN-lgr >= 0.3.4
Requires:         R-CRAN-mlr3tuning >= 0.14.0
Requires:         R-CRAN-mlr3 >= 0.14.0
Requires:         R-CRAN-mlr3misc >= 0.11.0
Requires:         R-CRAN-paradox >= 0.10.0
Requires:         R-CRAN-data.table 

%description
A modern and flexible approach to Bayesian Optimization / Model Based
Optimization building on the 'bbotk' package. 'mlr3mbo' is a toolbox
providing both ready-to-use optimization algorithms as well as their
fundamental building blocks allowing for straightforward implementation of
custom algorithms. Single- and multi-objective optimization is supported
as well as mixed continuous, categorical and conditional search spaces.
Moreover, using 'mlr3mbo' for hyperparameter optimization of machine
learning models within the 'mlr3' ecosystem is straightforward via
'mlr3tuning'. Examples of ready-to-use optimization algorithms include
Efficient Global Optimization by Jones et al. (1998)
<doi:10.1023/A:1008306431147>, ParEGO by Knowles (2006)
<doi:10.1109/TEVC.2005.851274> and SMS-EGO by Ponweiser et al. (2008)
<doi:10.1007/978-3-540-87700-4_78>.

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

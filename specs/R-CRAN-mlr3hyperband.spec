%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3hyperband
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hyperband for 'mlr3'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.9.4
BuildRequires:    R-CRAN-bbotk >= 1.6.0
BuildRequires:    R-CRAN-mlr3tuning >= 1.4.0
BuildRequires:    R-CRAN-paradox >= 0.9.0
BuildRequires:    R-CRAN-mlr3 >= 0.13.1
BuildRequires:    R-CRAN-mlr3misc >= 0.10.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lgr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-checkmate >= 1.9.4
Requires:         R-CRAN-bbotk >= 1.6.0
Requires:         R-CRAN-mlr3tuning >= 1.4.0
Requires:         R-CRAN-paradox >= 0.9.0
Requires:         R-CRAN-mlr3 >= 0.13.1
Requires:         R-CRAN-mlr3misc >= 0.10.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lgr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-uuid 

%description
Successive Halving (Jamieson and Talwalkar (2016)
<doi:10.48550/arXiv.1502.07943>) and Hyperband (Li et al. 2018
<doi:10.48550/arXiv.1603.06560>) optimization algorithm for the mlr3
ecosystem. The implementation in mlr3hyperband features improved
scheduling and parallelizes the evaluation of configurations. The package
includes tuners for hyperparameter optimization in mlr3tuning and
optimizers for black-box optimization in bbotk.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3tuning
%global packver   0.16.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tuning for 'mlr3'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-bbotk >= 0.7.0
BuildRequires:    R-CRAN-mlr3 >= 0.14.1
BuildRequires:    R-CRAN-mlr3misc >= 0.11.0
BuildRequires:    R-CRAN-paradox >= 0.10.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lgr 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-bbotk >= 0.7.0
Requires:         R-CRAN-mlr3 >= 0.14.1
Requires:         R-CRAN-mlr3misc >= 0.11.0
Requires:         R-CRAN-paradox >= 0.10.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lgr 
Requires:         R-CRAN-R6 

%description
Implements methods for hyperparameter tuning with 'mlr3', e.g. grid
search, random search, generalized simulated annealing and iterated
racing.  Various termination criteria can be set and combined.  The class
'AutoTuner' provides a convenient way to perform nested resampling in
combination with 'mlr3'.

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

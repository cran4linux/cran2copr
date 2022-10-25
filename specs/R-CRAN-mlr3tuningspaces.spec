%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3tuningspaces
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Search Spaces for Hyperparameter Tuning

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.5.0
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-paradox >= 0.7.1
BuildRequires:    R-CRAN-mlr3tuning >= 0.15.0
BuildRequires:    R-CRAN-mlr3 >= 0.11.0
BuildRequires:    R-CRAN-mlr3misc >= 0.11.0
Requires:         R-CRAN-R6 >= 2.5.0
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-paradox >= 0.7.1
Requires:         R-CRAN-mlr3tuning >= 0.15.0
Requires:         R-CRAN-mlr3 >= 0.11.0
Requires:         R-CRAN-mlr3misc >= 0.11.0

%description
Collection of search spaces for hyperparameter tuning. Includes various
search spaces that can be directly applied on an `mlr3` learner.
Additionally, meta information about the search space can be queried.

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

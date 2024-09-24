%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  optRF
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimising Random Forest Stability Through Selection of the Optimal Number of Trees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.2
Requires:         R-core >= 4.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-minpack.lm >= 1.2.4
BuildRequires:    R-CRAN-irr >= 0.84.1
BuildRequires:    R-CRAN-ranger >= 0.16.0
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-minpack.lm >= 1.2.4
Requires:         R-CRAN-irr >= 0.84.1
Requires:         R-CRAN-ranger >= 0.16.0
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 

%description
Calculating the stability of random forest with certain numbers of trees.
The non-linear relationship between stability and numbers of trees is
described using a logistic regression model and used to estimate the
optimal number of trees.

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

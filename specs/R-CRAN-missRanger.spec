%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  missRanger
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Imputation of Missing Values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-FNN 
Requires:         R-stats 
Requires:         R-utils 

%description
Alternative implementation of the beautiful 'MissForest' algorithm used to
impute mixed-type data sets by chaining random forests, introduced by
Stekhoven, D.J. and Buehlmann, P. (2012)
<doi:10.1093/bioinformatics/btr597>. Under the hood, it uses the lightning
fast random jungle package 'ranger'. Between the iterative model fitting,
we offer the option of using predictive mean matching. This firstly avoids
imputation with values not already present in the original data (like a
value 0.3334 in 0-1 coded variable).  Secondly, predictive mean matching
tries to raise the variance in the resulting conditional distributions to
a realistic level. This would allow e.g. to do multiple imputation when
repeating the call to missRanger().  A formula interface allows to control
which variables should be imputed by which.

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

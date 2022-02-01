%global __brp_check_rpaths %{nil}
%global packname  outForest
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Outlier Detection and Replacement

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-missRanger >= 2.1.0
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-missRanger >= 2.1.0
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-FNN 
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides a random forest based implementation of the method described in
Chapter 7.1.2 (Regression model based anomaly detection) of Chandola et
al. (2009) <doi:10.1145/1541880.1541882>. It works as follows: Each
numeric variable is regressed onto all other variables by a random forest.
If the scaled absolute difference between observed value and out-of-bag
prediction of the corresponding random forest is suspiciously large, then
a value is considered an outlier. The package offers different options to
replace such outliers, e.g. by realistic values found via predictive mean
matching. Once the method is trained on a reference data, it can be
applied to new data.

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

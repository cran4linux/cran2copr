%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  zoo
%global packver   1.9-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          S3 Infrastructure for Regular and Irregular Time Series (Z's Ordered Observations)

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-lattice >= 0.20.27
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-lattice >= 0.20.27
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
An S3 class with methods for working with regular and irregular time
series. The class stores data as numeric vectors/matrices (or factors)
along with a time index of arbitrary class (including numeric, Date,
POSIXct, chron, yearmon, yearqtr, etc.). Functions and methods are
consistent with the ts class and base R and also extend standard generics.
Tools include: Data import/export, coercion, visualization (with base R,
'ggplot2', 'lattice', 'tinyplot'), alignment and merging, aggregation,
lags and subsets, rolling analytics, and time-based interpolation/filling.
The design is introduced in Zeileis and Grothendieck (2005)
<doi:10.18637/jss.v014.i06>.

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

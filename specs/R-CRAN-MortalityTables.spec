%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MortalityTables
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          A Framework for Various Types of Mortality / Life Tables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-scales 
Requires:         R-utils 
Requires:         R-CRAN-pracma 

%description
Classes to implement and plot cohort life tables for actuarial
calculations. In particular, birth-year dependent mortality tables using a
yearly trend to extrapolate from a base year are implemented, as well as
period life table, cohort life tables using an age shift, and merged life
tables.

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

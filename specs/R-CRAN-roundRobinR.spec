%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  roundRobinR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Manipulate and Analyze Round Robin Dyadic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme >= 3.1.150
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-stats 
Requires:         R-CRAN-nlme >= 3.1.150
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-stats 

%description
Provides utilities for processing and analyzing dyadic data collected
using a round-robin design, in which each person in a group rates or
interacts with every other person on at least one variable. Data
manipulation functions prepare datasets for dyadic data analysis by
creating the actor and partner dummy variables required by the social
relations model (SRM). Analysis functions implement the SRM using
multilevel modeling via a custom 'nlme' covariance class ('pdSRM'),
following the approach of Snijders and Kenny (1999)
<doi:10.1111/j.1475-6811.1999.tb00204.x> and Knight and Humphrey (2019)
<doi:10.1037/0000115-019>. The package estimates group, actor, partner,
and relationship variance components along with generalized and dyadic
reciprocity correlations, and supports both null and fixed-effects models.

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

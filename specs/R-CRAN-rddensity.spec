%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rddensity
%global packver   2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Manipulation Testing Based on Density Discontinuity

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpdensity >= 2.2
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-lpdensity >= 2.2
Requires:         R-CRAN-ggplot2 

%description
Density discontinuity testing (a.k.a. manipulation testing) is commonly
employed in regression discontinuity designs and other program evaluation
settings to detect perfect self-selection (manipulation) around a cutoff
where treatment/policy assignment changes. This package implements
manipulation testing procedures using the local polynomial density
estimators: rddensity() to construct test statistics and p-values given a
prespecified cutoff, rdbwdensity() to perform data-driven bandwidth
selection, and rdplotdensity() to construct density plots.

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

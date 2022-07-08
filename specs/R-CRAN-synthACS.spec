%global __brp_check_rpaths %{nil}
%global packname  synthACS
%global packver   1.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Synthetic Microdata and Spatial MicroSimulation Modeling for ACS Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-acs >= 2.1
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-acs >= 2.1
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-Rcpp 

%description
Provides access to curated American Community Survey (ACS) base tables via
a wrapper to library(acs). Builds synthetic micro-datasets at any
user-specified geographic level with ten default attributes; and, conducts
spatial microsimulation modeling (SMSM) via simulated annealing.  SMSM is
conducted in parallel by default. Lastly, we provide functionality for
data-extensibility of micro-datasets.

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

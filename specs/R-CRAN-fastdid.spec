%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastdid
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Staggered Difference-in-Difference Estimators

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dreamerr >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-BMisc 
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-parglm 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-dreamerr >= 1.4.0
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-BMisc 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-parglm 
Requires:         R-CRAN-ggplot2 

%description
A fast and flexible implementation of Callaway and Sant'Anna's
(2021)<doi:10.1016/j.jeconom.2020.12.001> staggered
Difference-in-Differences (DiD) estimators, 'fastdid' reduces the
computation time from hours to seconds, and incorporates extensions such
as time-varying covariates and multiple events.

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

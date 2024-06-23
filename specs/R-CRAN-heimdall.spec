%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  heimdall
%global packver   1.0.707
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.707
Release:          1%{?dist}%{?buildtag}
Summary:          Drift Adaptable Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-daltoolbox 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-caret 
Requires:         R-stats 
Requires:         R-CRAN-daltoolbox 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reticulate 

%description
By analyzing streaming datasets, it is possible to observe significant
changes in the data distribution or models' accuracy during their
prediction (concept drift). The goal of 'heimdall' is to measure when
concept drift occurs. The package makes available several state-of-the-art
methods. It also tackles how to adapt models in a nonstationary context.
Some concept drifts methods are described in Tavares (2022)
<doi:10.1007/s12530-021-09415-z>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ecotrends
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Temporal Trends in Ecological Niche Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-fuzzySim >= 4.26
BuildRequires:    R-CRAN-modEvA >= 3.21
BuildRequires:    R-CRAN-terra >= 1.4.19
BuildRequires:    R-CRAN-maxnet 
BuildRequires:    R-CRAN-trend 
Requires:         R-CRAN-fuzzySim >= 4.26
Requires:         R-CRAN-modEvA >= 3.21
Requires:         R-CRAN-terra >= 1.4.19
Requires:         R-CRAN-maxnet 
Requires:         R-CRAN-trend 

%description
Computes temporal trends in environmental suitability obtained from
ecological niche models, based on a set of species presence point
coordinates and predictor variables.

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

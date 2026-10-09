%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  land4health
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Remote Sensing Metrics for Spatial Health Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rgee 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-ows4R 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rgee 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-ows4R 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-terra 

%description
Calculate and extract remote sensing metrics for spatial analysis in the
field of health. The package offers R users a quick and straightforward
way to obtain areal or zonal statistics of key environmental indicators,
covariates, and vector-borne disease data ideal for modeling infectious
diseases within the framework of spatial epidemiology.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcamelsCL
%global packver   0.1-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Handling of the CAMELS-CL Dataset

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.7.78
BuildRequires:    R-CRAN-zoo >= 1.7.2
BuildRequires:    R-CRAN-hydroTSM >= 0.5.0
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-terra >= 1.7.78
Requires:         R-CRAN-zoo >= 1.7.2
Requires:         R-CRAN-hydroTSM >= 0.5.0
Requires:         R-CRAN-httr 

%description
Download and handle spatial and temporal data from the CAMELS-CL dataset
(Catchment Attributes and Meteorology for Large Sample Studies, Chile)
<https://camels.cr2.cl/>, developed by Alvarez-Garreton et al. (2018)
<doi:10.5194/hess-22-5817-2018>. The package does not generate new data,
it only facilitates direct access to the original dataset for hydrological
analyses.

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

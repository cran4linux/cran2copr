%global __brp_check_rpaths %{nil}
%global packname  blockCV
%global packver   2.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial and Environmental Blocking for K-Fold Cross-Validation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-sf >= 0.8.0
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-sf >= 0.8.0
Requires:         R-CRAN-progress 

%description
Creating spatially or environmentally separated folds for cross-validation
to provide a robust error estimation in spatially structured environments;
Investigating and visualising the effective range of spatial
autocorrelation in continuous raster covariates to find an initial
realistic distance band to separate training and testing datasets
spatially described in Valavi, R. et al. (2019)
<doi:10.1111/2041-210X.13107>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

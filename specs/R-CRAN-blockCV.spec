%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blockCV
%global packver   3.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial and Environmental Blocking for K-Fold and LOO Cross-Validation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-terra >= 1.6.41
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-automap >= 1.0.16
BuildRequires:    R-CRAN-sf >= 1.0
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-cowplot 
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-terra >= 1.6.41
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-automap >= 1.0.16
Requires:         R-CRAN-sf >= 1.0
Requires:         R-CRAN-sp 
Requires:         R-CRAN-cowplot 

%description
Creating spatially or environmentally separated folds for cross-validation
to provide a robust error estimation in spatially structured environments;
Investigating and visualising the effective range of spatial
autocorrelation in continuous raster covariates and point samples to find
an initial realistic distance band to separate training and testing
datasets spatially described in Valavi, R. et al. (2019)
<doi:10.1111/2041-210X.13107>.

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

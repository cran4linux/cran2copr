%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blockCV
%global packver   4.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial and Environmental Blocking for Cross-Validation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-terra >= 1.6.41
BuildRequires:    R-CRAN-automap >= 1.1.20
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-sf >= 1.0
BuildRequires:    R-CRAN-cowplot 
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-terra >= 1.6.41
Requires:         R-CRAN-automap >= 1.1.20
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-sf >= 1.0
Requires:         R-CRAN-cowplot 

%description
Creates spatially or environmentally separated, or group-preserving,
training and testing folds for k-fold, leave-group-out, and leave-one-out
cross-validation. Provides spatial blocking, clustering, buffering, and
nearest-neighbour distance-matching methods, together with tools to
visualise folds, summarise fold sizes and class balance, and assess
train–test separation and environmental novelty. Also estimates spatial
autocorrelation ranges in point samples and continuous raster covariates
to provide an initial distance scale for designing spatial folds. Methods
are described in Valavi, R. et al. (2019) <doi:10.1111/2041-210X.13107>.

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

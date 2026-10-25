%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flexsdm
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Species Distribution Modeling Workflow

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-terra >= 1.5.21
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-maxnet 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-spThin 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-terra >= 1.5.21
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gbm 
Requires:         R-grDevices 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-maxnet 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-spThin 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-Rcpp 

%description
Provides a flexible and comprehensive workflow for species distribution
modeling, from data preparation (occurrence filtering, calibration areas,
pseudo-absence and background sampling, data partitioning, and
collinearity reduction) to model fitting, tuning, evaluation, prediction,
ensemble modeling, and post-processing. The package is described in
Velazco et al. (2022) <doi:10.1111/2041-210X.13874>. Implemented methods
include the Shape metric to measure model extrapolation of Velazco et al.
(2023) <doi:10.1111/ecog.06992>, ensembles of small models of Breiner et
al. (2015) <doi:10.1111/2041-210X.12403> and Breiner et al. (2018)
<doi:10.1111/2041-210X.12957>, Gaussian process models of Golding and
Purse (2016) <doi:10.1111/2041-210X.12523>, and occurrence-based
constraints for post-processing predictions of Mendes et al. (2020)
<doi:10.1016/j.ecolmodel.2020.109180>.

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

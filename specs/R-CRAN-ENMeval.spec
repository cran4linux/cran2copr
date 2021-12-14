%global __brp_check_rpaths %{nil}
%global packname  ENMeval
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Tuning and Evaluations of Ecological Niche Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-maxnet 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-rangeModelMetadata 
BuildRequires:    R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-maxnet 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-rangeModelMetadata 
Requires:         R-CRAN-rlang 

%description
Runs ecological niche models over all combinations of user-defined
settings (i.e., tuning), performs cross validation to evaluate models, and
returns data tables to aid in selection of optimal model settings that
balance goodness-of-fit and model complexity. Also has functions to
partition data spatially (or not) for cross validation, to plot multiple
visualizations of results, to run null models to estimate significance and
effect sizes of performance metrics, and to calculate niche overlap
between model predictions, among others. The package was originally built
for Maxent models (Phillips et al. 2006, Phillips et al. 2017), but the
current version allows possible extensions for any modeling algorithm. The
extensive vignette, which guides users through most package functionality
but unfortunately has a file size too big for CRAN, can be found here on
the package's Github Pages website:
<https://jamiemkass.github.io/ENMeval/articles/ENMeval-2.0.0-vignette.html>.

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

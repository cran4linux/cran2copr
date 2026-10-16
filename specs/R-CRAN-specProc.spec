%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  specProc
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          Preprocessing Tools for Laser-Induced Breakdown Spectroscopy

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Tools for exploring, preprocessing and modeling spectroscopic data,
developed for laser-induced breakdown spectroscopy (LIBS) and also
applicable to other techniques such as Raman, infrared, and inductively
coupled plasma optical emission spectroscopy. Covers the workflow from raw
spectra to calibrated results: peak finding and fitting, wavelength
calibration, baseline correction, normalization and scaling, orthogonal
signal correction including orthogonal partial least squares (OPLS; Trygg
and Wold (2002) <doi:10.1002/cem.695>), calibration transfer, calibration
curves and figures of merit, and plasma diagnostics (Boltzmann and
Saha-Boltzmann plots, Stark broadening). Includes robust tools for outlier
detection and exploration: robust principal component analysis (Hubert,
Rousseeuw and Vanden Branden (2005) <doi:10.1198/004017004000000563>),
detection of deviating cells (Rousseeuw and Van den Bossche (2018)
<doi:10.1080/00401706.2017.1340909>), PCA with cellwise outliers and
missing values (MacroPCA; Hubert, Rousseeuw and Van den Bossche (2019)
<doi:10.1080/00401706.2018.1562989>), robust transformations to central
normality (Raymaekers and Rousseeuw (2021)
<doi:10.1007/s10994-021-05960-5>), and self-organizing maps (Kohonen
(1982) <doi:10.1007/BF00337288>). Preprocessing steps are also available
as 'recipes' steps for 'tidymodels' workflows. Computationally intensive
steps are implemented in 'C++' via 'Rcpp' and 'RcppEigen'.

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

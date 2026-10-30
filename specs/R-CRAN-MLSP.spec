%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MLSP
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Models for Soil Properties from Spectroscopy

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gsignal 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Cubist 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-gsignal 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Cubist 
Requires:         R-CRAN-randomForest 

%description
Soil spectroscopy studies use many different combinations of spectral
preprocessing and calibration methods, which makes results difficult to
compare or generalize across studies. For visible and near-infrared (VNIR)
spectra (350-2500 nm), runs every combination of preprocessing and
calibration methods on identical repeated calibration and validation
splits. The 26 preprocessing methods are raw reflectance, standard normal
variate, pseudo-absorbance, and 23 Savitzky-Golay smoothers, first
derivatives, and second derivatives with linear, quadratic, or cubic
polynomials and 3- to 11-point windows, excluding settings that give
mathematically identical filters. The calibration methods are principal
component regression (PCR), partial least squares regression (PLSR), least
absolute shrinkage and selection operator (LASSO), 'Cubist', and random
forest. Model complexity is tuned by cross-validation within each
calibration set, and combinations are ranked by the coefficient of
determination (R2), root mean squared error (RMSE), ratio of performance
to interquartile distance (RPIQ), or bias, reporting the top 10 by
default. The methods are those most commonly used in published soil
spectroscopy studies, following Savitzky and Golay (1964)
<doi:10.1021/ac60214a047>, Barnes et al. (1989)
<doi:10.1366/0003702894202201>, Rinnan et al. (2009)
<doi:10.1016/j.trac.2009.07.007>, Bellon-Maurel et al. (2010)
<doi:10.1016/j.trac.2010.05.006>, and Clingensmith et al. (2019)
<doi:10.1111/ejss.12753>.

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

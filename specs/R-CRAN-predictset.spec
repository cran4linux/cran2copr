%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  predictset
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conformal Prediction and Uncertainty Quantification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Implements conformal prediction methods for constructing prediction
intervals (regression) and prediction sets (classification) with
finite-sample coverage guarantees. Methods include split conformal, 'CV+'
and 'Jackknife+' (Barber et al. 2021) <doi:10.1214/20-AOS1965>,
'Conformalized Quantile Regression' (Romano et al. 2019)
<doi:10.48550/arXiv.1905.03222>, 'Adaptive Prediction Sets' (Romano,
Sesia, Candes 2020) <doi:10.48550/arXiv.2006.02544>, 'Regularized Adaptive
Prediction Sets' (Angelopoulos et al. 2021)
<doi:10.48550/arXiv.2009.14193>, Mondrian conformal prediction for
group-conditional coverage (Vovk et al. 2005), weighted conformal
prediction for covariate shift (Tibshirani et al. 2019), and adaptive
conformal inference for sequential prediction (Gibbs and Candes 2021). All
methods are distribution-free and provide calibrated uncertainty
quantification without parametric assumptions. Works with any model that
can produce predictions from new data, including 'lm', 'glm', 'ranger',
'xgboost', and custom user-defined models.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  probcal
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calibration of Binary and Multiclass Probabilities

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-withr 

%description
Provides S3 calibrators, metrics, and diagnostics for binary and
multiclass probability calibration. Binary methods include Platt scaling,
temperature scaling, beta calibration, histogram binning, and isotonic
regression. Multiclass methods include temperature scaling, vector
scaling, Dirichlet calibration, and a one-vs-rest wrapper for the binary
calibrators. A calibration-inference layer adds debiased calibration
errors, bootstrap confidence intervals, and a kernel calibration
hypothesis test for binary and multiclass predictions, including the
strong (canonical) multiclass case. Methods follow Platt (1999,
ISBN:9780262194488), Zadrozny and Elkan (2002)
<doi:10.1145/775047.775151>, Guo et al. (2017)
<https://proceedings.mlr.press/v70/guo17a.html>, Kull et al. (2017)
<doi:10.1214/17-EJS1338SI>, Kull et al. (2019)
<doi:10.48550/arXiv.1910.12656>, Widmann et al. (2019)
<doi:10.48550/arXiv.1910.11385>, and Kumar et al. (2019)
<doi:10.48550/arXiv.1909.10155>.

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

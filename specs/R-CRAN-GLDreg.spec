%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GLDreg
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fit GLD Regression/Quantile/AFT Model to Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GLDEX >= 2.0.0.5
BuildRequires:    R-CRAN-ddst 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-GLDEX >= 2.0.0.5
Requires:         R-CRAN-ddst 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Owing to the rich shapes of Generalised Lambda Distributions (GLDs), GLD
standard/quantile/Accelerated Failure Time (AFT) regression is a
competitive flexible model compared to standard/quantile/AFT regression.
The proposed method has some major advantages: 1) it provides a reference
line which is very robust to outliers with the attractive property of zero
mean residuals and 2) it gives a unified, elegant quantile regression
model from the reference line with smooth regression coefficients across
different quantiles. For AFT model, it also eliminates the needs to try
several different AFT models, owing to the flexible shapes of GLD. The
goodness of fit of the proposed model can be assessed via QQ plots and
Kolmogorov-Smirnov tests and data driven smooth test, to ensure the
appropriateness of the statistical inference under consideration.
Statistical distributions of coefficients of the GLD regression line are
obtained using simulation, and interval estimates are obtained directly
from simulated data.  References include the following: Su (2015)
"Flexible Parametric Quantile Regression Model"
<doi:10.1007/s11222-014-9457-1>, Su (2021) "Flexible parametric
accelerated failure time model"<doi:10.1080/10543406.2021.1934854>.

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

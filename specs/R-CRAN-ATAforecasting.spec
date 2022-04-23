%global __brp_check_rpaths %{nil}
%global packname  ATAforecasting
%global packver   0.0.57
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.57
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Time Series Analysis and Forecasting using the Ata Method

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-seasonal 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stlplus 
BuildRequires:    R-CRAN-stR 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-TSA 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-graphics 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-seasonal 
Requires:         R-stats 
Requires:         R-CRAN-stlplus 
Requires:         R-CRAN-stR 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-TSA 
Requires:         R-CRAN-tseries 
Requires:         R-utils 
Requires:         R-CRAN-xts 

%description
The Ata method (Yapar et al. (2019) <doi:10.15672/hujms.461032>), an
alternative to exponential smoothing (described in Yapar (2016)
<doi:10.15672/HJMS.201614320580>, Yapar et al. (2017)
<doi:10.15672/HJMS.2017.493>), is a new univariate time series forecasting
method which provides innovative solutions to issues faced during the
initialization and optimization stages of existing forecasting methods.
Forecasting performance of the Ata method is superior to existing methods
both in terms of easy implementation and accurate forecasting. It can be
applied to non-seasonal or seasonal time series which can be decomposed
into four components (remainder, level, trend and seasonal). This
methodology performed well on the M3 and M4-competition data. This package
was written based on Ali Sabri Taylan’s PhD dissertation.

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

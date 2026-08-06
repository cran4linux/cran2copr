%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  predHCS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Point and Interval Prediction for Censored Data under Various Hybrid Censoring Schemes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Implements generalized statistical point prediction and prediction
intervals for future failure times under various hybrid censoring schemes.
Supported censoring schemes include Type-I, Type-II, Generalized Type-I,
Generalized Type-II, Unified, Progressive Type-I, and Progressive Type-II
hybrid censoring schemes. Available prediction methods include Best
Unbiased Predictor (BUP), Conditional Median Predictor (CMP), Maximum
Likelihood Predictor (MLP), equal-tailed classical prediction intervals,
Highest Conditional Density (HCD) prediction intervals, and Bayesian
prediction intervals. Algorithms accept user-defined continuous
probability density functions, cumulative distribution functions, quantile
functions, or survival functions along with estimated parameter values.
Methodological foundations are based on Balakrishnan, Cramer, and Kundu
(2023, ISBN:978-0123983879), Shafay and Balakrishnan (2012)
<doi:10.1080/03610918.2011.579367> for Type-I hybrid censoring,
Balakrishnan and Shafay (2012) <doi:10.1080/03610926.2010.543300> for
Type-II hybrid censoring, Shafay (2017)
<doi:10.1080/03610926.2016.1200093> for Generalized Type-I hybrid
censoring, Shafay (2016) <doi:10.1080/00949655.2015.1096361> for
Generalized Type-II hybrid censoring, Mohie El-Din, Nagy, and Shafay
(2017) <doi:10.18576/jsap/060113> for Unified hybrid censoring, Ebrahimi
(1992) <doi:10.1109/24.126685>, Valiollahi, Asgharzadeh, and Kundu (2017)
<doi:10.1214/15-BJPS302>, and Asgharzadeh, Valiollahi, and Kundu (2015)
<doi:10.1080/00949655.2013.848451>.

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

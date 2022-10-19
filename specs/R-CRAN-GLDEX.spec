%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GLDEX
%global packver   2.0.0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Single and Mixture of Generalised Lambda Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-spacefillr 
Requires:         R-CRAN-cluster 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-spacefillr 

%description
The fitting algorithms considered in this package have two major
objectives. One is to provide a smoothing device to fit distributions to
data using the weight and unweighted discretised approach based on the bin
width of the histogram. The other is to provide a definitive fit to the
data set using the maximum likelihood and quantile matching estimation.
Other methods such as moment matching, starship method, L moment matching
are also provided. Diagnostics on goodness of fit can be done via qqplots,
KS-resample tests and comparing mean, variance, skewness and kurtosis of
the data with the fitted distribution. References include the following:
Karvanen and Nuutinen (2008) "Characterizing the generalized lambda
distribution by L-moments" <doi:10.1016/j.csda.2007.06.021>, King and
MacGillivray (1999) "A starship method for fitting the generalised lambda
distributions" <doi:10.1111/1467-842X.00089>, Su (2005) "A Discretized
Approach to Flexibly Fit Generalized Lambda Distributions to Data"
<doi:10.22237/jmasm/1130803560>, Su (2007) "Nmerical Maximum Log
Likelihood Estimation for Generalized Lambda Distributions"
<doi:10.1016/j.csda.2006.06.008>, Su (2007) "Fitting Single and Mixture of
Generalized Lambda Distributions to Data via Discretized and Maximum
Likelihood Methods: GLDEX in R" <doi:10.18637/jss.v021.i09>, Su (2009)
"Confidence Intervals for Quantiles Using Generalized Lambda
Distributions" <doi:10.1016/j.csda.2009.02.014>, Su (2010) "Chapter 14:
Fitting GLDs and Mixture of GLDs to Data using Quantile Matching Method"
<doi:10.1201/b10159>, Su (2010) "Chapter 15: Fitting GLD to data using
GLDEX 1.0.4 in R" <doi:10.1201/b10159>, Su (2015) "Flexible Parametric
Quantile Regression Model" <doi:10.1007/s11222-014-9457-1>, Su (2021)
"Flexible parametric accelerated failure time
model"<doi:10.1080/10543406.2021.1934854>.

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

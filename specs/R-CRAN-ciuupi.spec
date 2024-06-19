%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ciuupi
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Confidence Intervals Utilizing Uncertain Prior Information

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-functional 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-functional 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-graphics 

%description
Computes a confidence interval for a specified linear combination of the
regression parameters in a linear regression model with iid normal errors
with known variance when there is uncertain prior information that a
distinct specified linear combination of the regression parameters takes a
given value.  This confidence interval, found by numerical nonlinear
constrained optimization, has the required minimum coverage and utilizes
this uncertain prior information through desirable expected length
properties. This confidence interval has the following three practical
applications. Firstly, if the error variance has been accurately estimated
from previous data then it may be treated as being effectively known.
Secondly, for sufficiently large (dimension of the response vector) minus
(dimension of regression parameter vector), greater than or equal to 30
(say), if we replace the assumed known value of the error variance by its
usual estimator in the formula for the confidence interval then the
resulting interval has, to a very good approximation, the same coverage
probability and expected length properties as when the error variance is
known. Thirdly, some more complicated models can be approximated by the
linear regression model with error variance known when certain unknown
parameters are replaced by estimates. This confidence interval is
described in Mainzer, R. and Kabaila, P. (2019)
<doi:10.32614/RJ-2019-026>, and is a member of the family of confidence
intervals proposed by Kabaila, P. and Giri, K. (2009)
<doi:10.1016/j.jspi.2009.03.018>.

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

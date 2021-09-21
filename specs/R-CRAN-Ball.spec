%global __brp_check_rpaths %{nil}
%global packname  Ball
%global packver   1.3.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.12
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Inference and Sure Independence Screening via Ball Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-mvtnorm 

%description
Hypothesis tests and sure independence screening (SIS) procedure based on
ball statistics, including ball divergence <doi:10.1214/17-AOS1579>, ball
covariance <doi:10.1080/01621459.2018.1543600>, and ball correlation
<doi:10.1080/01621459.2018.1462709>, are developed to analyze complex data
in metric spaces, e.g, shape, directional, compositional and symmetric
positive definite matrix data. The ball divergence and ball covariance
based distribution-free tests are implemented to detecting distribution
difference and association in metric spaces <doi:10.18637/jss.v097.i06>.
Furthermore, several generic non-parametric feature selection procedures
based on ball correlation, BCor-SIS and all of its variants, are
implemented to tackle the challenge in the context of ultra high
dimensional data. A fast implementation for large-scale multiple K-sample
testing with ball divergence <doi: 10.1002/gepi.22423> is supported, which
is particularly helpful for genome-wide association study.

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

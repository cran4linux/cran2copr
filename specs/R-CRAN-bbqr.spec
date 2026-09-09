%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bbqr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Quantile Regression with Lasso and Adaptive Lasso

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Markov chain Monte Carlo samplers for Bayesian quantile regression, based
on the asymmetric Laplace distribution and the location-scale mixture
representation of Kozumi and Kobayashi (2011)
<doi:10.1080/00949655.2010.496117>. A binary response and an observed
continuous response are both supported, each with three penalty layers
behind one interface: no penalty, following Benoit and Van den Poel (2012)
<doi:10.1002/jae.1216>; the Bayesian lasso, following Benoit, Al-Hamzawi
and Yu (2013) <doi:10.1007/s00180-013-0439-0>; and the Bayesian adaptive
lasso of Rubio Garcia (2023)
<https://soar.wichita.edu/entities/publication/a2f86232-4704-4ec2-b685-751e7b04ec42>.
In the binary family each is available as published and in a corrected
form, the default, in which every improper prior component is replaced by
a proper one so that the posterior exists unconditionally; the continuous
family ships the corrected form only. The continuous adaptive-lasso layer
at its default reproduces the penalty of Alhamzawi, Yu and Benoit (2012)
<doi:10.1177/1471082X1101200304>. A binary threshold model identifies the
coefficient vector only up to a positive scale, so the binary samplers
expose the identification anchor as an explicit argument, allowing fixing
the scale of the error distribution, fixing a single coefficient, and
constraining the norm of the coefficient vector to be compared directly;
an observed response identifies the scale, so the continuous samplers have
no anchor and draw it every sweep. The MCMC cores are written in Fortran
and called from R.

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

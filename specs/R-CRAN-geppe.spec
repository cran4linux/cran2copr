%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geppe
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalised Exponential Poisson and Poisson Exponential Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rfast2 
Requires:         R-stats 

%description
Maximum likelihood estimation, random values generation, density
computation and other functions for the exponential-Poisson generalised
exponential-Poisson and Poisson-exponential distributions. References
include: Rodrigues G. C., Louzada F. and Ramos P. L. (2018).
"Poisson-exponential distribution: different methods of estimation".
Journal of Applied Statistics, 45(1): 128--144.
<doi:10.1080/02664763.2016.1268571>. Louzada F., Ramos, P. L. and
Ferreira, H. P. (2020). "Exponential-Poisson distribution: estimation and
applications to rainfall and aircraft data with zero occurrence".
Communications in Statistics--Simulation and Computation, 49(4):
1024--1043. <doi:10.1080/03610918.2018.1491988>. Barreto-Souza W. and
Cribari-Neto F. (2009). "A generalization of the exponential-Poisson
distribution". Statistics and Probability Letters, 79(24): 2493--2500.
<doi:10.1016/j.spl.2009.09.003>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chapensk
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Gas Properties from the Lennard-Jones Potential

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Bessel 
Requires:         R-methods 
Requires:         R-CRAN-Bessel 

%description
Estimation of gas transport properties (viscosity, diffusion, thermal
conductivity) using Chapman-Enskok theory (Chapman and Larmor 1918,
<doi:10.1098/rsta.1918.0005>) and of the second virial coefficient (Vargas
et al. 2001, <doi:10.1016/s0378-4371(00)00362-9>) using the Lennard-Jones
(12-6) potential. Up to the third order correction is taken into account
for viscosity and thermal conductivity. It is also possible to calculate
the binary diffusion coefficients of polar and non-polar gases in
non-polar bath gases (Brown et al. 2011,
<doi:10.1016/j.pecs.2010.12.001>). 16 collision integrals are calculated
with four digit accuracy over the reduced temperature range [0.3, 400]
using an interpolation function of Kim and Monroe (2014,
<doi:10.1016/j.jcp.2014.05.018>).

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

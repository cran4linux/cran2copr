%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rsdNE
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Response Surface Designs with Neighbour Effects (rsdNE)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Response surface designs with neighbour effects are suitable for
experimental situations where it is expected that the treatment
combination administered to one experimental unit may affect the response
on neighboring units as well as the response on the unit to which it is
applied (Dalal et al.,2025 <doi: 10.57805/revstat.v23i2.513>). Integrating
these effects in the response surface model improves the experiment's
precision Verma A., Jaggi S., Varghese, E.,Varghese, C.,Bhowmik, A.,
Datta, A. and Hemavathi M. (2021)<doi: 10.1080/03610918.2021.1890123>).
This package includes sym(), asym1(), asym2(), asym3() and asym4()
functions that generates response surface designs which are rotatable
under a polynomial model of a given order without interaction term
incorporating neighbour effects.

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

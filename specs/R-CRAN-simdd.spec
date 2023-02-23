%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simdd
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation of Fisher Bingham and Related Directional Distributions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Simulation methods for the Fisher Bingham distribution on the unit sphere,
the matrix Bingham distribution on a Grassmann manifold, the matrix Fisher
distribution on SO(3), and the bivariate von Mises sine model on the
torus. The methods use the first ever general purpose acceptance/rejection
simulation algorithm for the Bingham distribution and are described fully
by Kent, Ganeiber and Mardia (2018) <doi:10.1080/10618600.2017.1390468>.
These methods superseded earlier MCMC simulation methods and are more
general than earlier simulation methods. The methods can be slower in
specific situations where there are existing non-MCMC simulation methods
(see Section 8 of Kent, Ganeiber and Mardia (2018)
<doi:10.1080/10618600.2017.1390468> for further details).

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

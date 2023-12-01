%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  resevol
%global packver   0.3.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Agricultural Production and Evolution of Pesticide Resistance

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-utils >= 4.0.0
Requires:         R-stats >= 4.0.0
Requires:         R-utils >= 4.0.0

%description
Simulates individual-based models of agricultural pest management and the
evolution of pesticide resistance. Management occurs on a spatially
explicit landscape that is divided into an arbitrary number of farms that
can grow one of up to 10 crops and apply one of up to 10 pesticides. Pest
genomes are modelled in a way that allows for any number of pest traits
with an arbitrary covariance structure that is constructed using an
evolutionary algorithm in the mine_gmatrix() function. Simulations are
then run using the run_farm_sim() function. This package thereby allows
for highly mechanistic social-ecological models of the evolution of
pesticide resistance under different types of crop rotation and pesticide
application regimes.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PRNG
%global packver   0.0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Pseudo-Random Number Generator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides functions for generating pseudo-random numbers that follow a
uniform distribution [0,1]. Randomness tests were conducted using the
National Institute of Standards and Technology test
suite<https://csrc.nist.gov/pubs/sp/800/22/r1/upd1/final>, along with
additional tests. The sequence generated depends on the initial values and
parameters. The package includes a linear congruence map as the decision
map and three chaotic maps to generate the pseudo-random sequence, which
follow a uniform distribution. Other distributions can be generated from
the uniform distribution using the Inversion Principle Method and
BOX-Muller transformation. Small perturbations in seed values result in
entirely different sequences of numbers due to the sensitive nature of the
maps being used. The chaotic nature of the maps helps achieve randomness
in the generator. Additionally, the generator is capable of producing
random bits.

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

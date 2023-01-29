%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  randtoolbox
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Toolbox for Pseudo and Quasi Random Number Generation and Random Generator Tests

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rngWELL >= 0.10.1
Requires:         R-CRAN-rngWELL >= 0.10.1

%description
Provides (1) pseudo random generators - general linear congruential
generators, multiple recursive generators and generalized feedback shift
register (SF-Mersenne Twister algorithm
(<doi:10.1007/978-3-540-74496-2_36>) and WELL
(<doi:10.1145/1132973.1132974>) generators); (2) quasi random generators -
the Torus algorithm, the Sobol sequence, the Halton sequence (including
the Van der Corput sequence) and (3) some generator tests - the gap test,
the serial test, the poker test, see, e.g., Gentle (2003)
<doi:10.1007/b97336>. Take a look at the Distribution task view of types
and tests of random number generators. The package can be provided without
the 'rngWELL' dependency on demand. Package in Memoriam of Diethelm and
Barbara Wuertz.

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

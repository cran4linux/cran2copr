%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  zuyaml
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parse and Emit 'YAML' 1.2

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Converts between 'YAML' 1.2 (<https://yaml.org/spec/1.2.2/>) and ordinary
R objects using a bundled copy of the 'cyaml' C11 parser and emitter
(<https://github.com/andrewmd5/cyaml>), so there is no system dependency
and no runtime dependency beyond R itself. Ambiguous 'YAML' features are
handled strictly and predictably: duplicate keys are refused by default,
the 'YAML' 1.2 core schema is followed so that yes and no resolve as
strings, and integers beyond double precision are preserved rather than
silently rounded. A stream of documents and a sequence are different
things, and the interface keeps them apart. Input size, nesting depth and
the number of values materialised are all bounded, which makes the parser
usable on untrusted input.

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

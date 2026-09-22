%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  raddr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Show What an IP Address Literal Means Under Every Standard

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.7
BuildRequires:    R-CRAN-vctrs >= 0.7.0
Requires:         R-CRAN-rlang >= 1.1.7
Requires:         R-CRAN-vctrs >= 0.7.0

%description
Standards and implementations disagree about what an IP address literal
means: the string "0177.0.0.1" is rejected by the dotted-quad grammar,
read as 127.0.0.1 by browsers, and read as 177.0.0.1 by some 'inet_pton'
implementations. Most libraries pick one reading and discard the rest.
This package reports them all, alongside the reason codes that explain
each one, and classifies parsed values against the IANA special-purpose
address registries. It is pure R, performs no network access, and returns
facts rather than allow or deny verdicts.

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

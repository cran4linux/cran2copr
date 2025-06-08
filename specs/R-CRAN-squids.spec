%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  squids
%global packver   25.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          25.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Short Quasi-Unique Identifiers (SQUIDs)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
It is often useful to produce short, quasi-unique identifiers (SQUIDs)
without the benefit of a central authority to prevent duplication.
Although Universally Unique Identifiers (UUIDs) provide for this, these
are also unwieldy; for example, the most used UUID, version 4, is 36
characters long. SQUIDs are short (8 characters) at the expense of having
more collisions, which can be mitigated by combining them with
human-produced suffixes, yielding relatively brief, half human-readable,
almost-unique identifiers (see for example the identifiers used for
Decentralized Construct Taxonomies; Peters & Crutzen, 2024
<doi:10.15626/MP.2022.3638>). SQUIDs are the number of centiseconds
elapsed since the beginning of 1970 converted to a base 30 system. This
package contains functions to produce SQUIDs as well as convert them back
into dates and times.

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

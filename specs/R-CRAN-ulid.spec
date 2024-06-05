%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ulid
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Universally Unique 'Lexicographically' 'Sortable' Identifiers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Universally unique identifiers ('UUIDs') can be sub-optimal for many
uses-cases because they are not the most character efficient way of
encoding 128 bits of randomness; v1/v2 versions are impractical in many
environments, as they require access to a unique, stable MAC address;
v3/v5 versions require a unique seed and produce randomly distributed IDs,
which can cause fragmentation in many data structures; v4 provides no
other information than randomness which can cause fragmentation in many
data structures. Providing an alternative, 'ULIDs'
(<https://github.com/ulid/spec>) have 128-bit compatibility with 'UUID',
1.21e+24 unique 'ULIDs' per millisecond, support standard (text) sorting,
canonically encoded as a 26 character string, as opposed to the 36
character 'UUID', use 'base32' encoding for better efficiency and
readability (5 bits per character), are case insensitive, have no special
characters (i.e. are 'URL' safe) and have a monotonic sort order
(correctly detects and handles the same millisecond).

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

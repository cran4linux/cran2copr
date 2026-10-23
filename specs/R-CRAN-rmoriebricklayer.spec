%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmoriebricklayer
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Data Capsules with Provenance and Fallback

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
For analyzing published and unpublished tables, from open-data portals and
statistical agencies to a researcher's own data, so that a result can be
traced to the exact data behind it and checked again afterwards. A
'capsule' records where each source came from, its Secure Hash Algorithm
256 ('SHA-256') hash, the schema it should have and an archived copy in
the Internet Archive 'Wayback Machine' ('web.archive.org'); sources are
found through the Comprehensive Knowledge Archive Network ('CKAN',
'ckan.org'). Run again, a capsule says whether each source still matches
and, if it does not, how its distribution moved (Kolmogorov-Smirnov,
chi-square, population stability index and 'Benford' first-digit screens),
and when a source cannot be reached it runs on schema-driven synthetic
data that is marked as such. Capsules can be signed with keyed hashes
('HMAC-SHA-256', RFC 2104) or with the post-quantum signature standards
'ML-DSA' (FIPS 204), 'SLH-DSA' (FIPS 205) and 'XMSS' (RFC 8391),
implemented from the standards with no system cryptography library and
checked against 'OpenSSL' 3.5 and the known-answer vectors of 'NIST' (the
US National Institute of Standards and Technology). For the administrative
tables these capsules usually hold, it computes period-over-period change
with exact intervals, trends (Mann-Kendall with 'Theil-Sen' slopes),
rates, and the bounds that rounding and suppression in a release imply;
small-area rates with the empirical Bayes shrinkage of Clayton and
'Kaldor' (1987) DOI 10.2307/2532003; self-exciting event series as
'Hawkes' processes; custodial populations by stock-and-flow measures; and
the burden of air pollution from dispersion to attributable deaths.

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

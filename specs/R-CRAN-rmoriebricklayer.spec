%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmoriebricklayer
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Data Capsules with Provenance and Fallback

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools for building brick-proof, reproducible, self-contained data
capsules. Resolves open-data sources through the Comprehensive Knowledge
Archive Network ('CKAN', <https://ckan.org/>) package_show and
package_search endpoints, records and verifies provenance with Secure Hash
Algorithm 256 ('SHA-256') digests and Internet Archive 'Wayback Machine'
(<https://web.archive.org/>) snapshots, validates downloaded data against
a pinned schema, and falls back to schema-driven synthetic data when the
real source is unreachable. Run records are captured in a manifest plus a
plain-language summary so any result can be traced back to its inputs.
Distributional drift between a pinned capsule and a fresh fetch is tested
with Kolmogorov-Smirnov, chi-square, population stability index,
Jensen-Shannon divergence and 'Benford' first-digit screens, because a
re-released extract can be statistically identical yet differ
byte-for-byte, and a column can keep its name and type while having been
silently rescaled. Manifests can be authenticated rather than only
checksum-verified, with keyed digests ('HMAC-SHA-256', RFC 2104) or
post-quantum hash-based signatures ('Winternitz' one-time signatures under
a 'Merkle' tree, RFC 8391), and pinned chunk-wise through a 'Merkle' tree
so a mismatch identifies which part of a capsule moved. Also ships a
compiled C++ core (summary, robust and rank statistics, 'SHA-256',
'SHA-512' and 'CRC-32') that sibling packages in the 'rmorie' ecosystem
reach through 'LinkingTo' for a single, shared numeric and
provenance-hashing backend. For the published administrative tables these
capsules usually hold, it computes period-over-period change matched on
the period rather than the row, with the exact conditional-binomial
interval for a ratio of counts and with a percentage-point reading kept
distinct from a percent change, rendered to Hypertext Markup Language
('HTML'), Portable Document Format ('PDF'), delimited text, JavaScript
Object Notation ('JSON') or Markdown. Interval categories such as "2 to 5"
or "50+" are parsed to bounds and the dependence of any derived figure on
the open top band is measured rather than assumed. Concentration is
summarised by the 'Gini' coefficient, the Lorenz curve and tail-index
estimation by exact discrete maximum likelihood; trend in a series of a
few periods by the Mann-Kendall test with 'Theil-Sen' slopes, a
permutation step-change scan and Poisson rate ratios; and region-coded
counts by indirect standardisation, exact standardised incidence ratios,
the empirical Bayes shrinkage of Clayton and 'Kaldor' (1987)
<doi:10.2307/2532003>, funnel-plot limits and Moran's I.

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

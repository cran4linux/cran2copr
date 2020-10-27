%global packname  swdpwr
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Power Calculation for Stepped Wedge Cluster Randomized Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
To meet the needs of statistical power calculation for stepped wedge
cluster randomized trials, we developed this software. Different
parameters can be specified by users for different scenarios, including:
cohort and cross-sectional settings, binary and continuous outcomes,
marginal (GEE) and conditional (mixed effect model) methods, different
link functions (identity, log, logit links), with and without time effect
of treatment, etc. The methods included in this package: Zhou et al.
(2020) <doi:10.1093/biostatistics/kxy031>, Li et al. (2018)
<doi:10.1111/biom.12918>. Supplementary documents can be found at:
<https://publichealth.yale.edu/cmips/research/software/swdpwr/>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

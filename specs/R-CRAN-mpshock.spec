%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mpshock
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Monetary Policy Shock Series for Empirical Macroeconomics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a curated multi-country collection of monetary policy shock and
stance series from the empirical macroeconomics literature, bundled as
tidy data frames with provenance metadata. Version 0.1.0 includes thirteen
series covering the United States, United Kingdom, and Australia: for the
US, the policy news shock of Nakamura and Steinsson (2018)
<doi:10.1093/qje/qjy004>, the orthogonalised surprise of Bauer and Swanson
(2023) <doi:10.1257/aer.20201220>, the target and path factors of the
Swanson (2021) <doi:10.1016/j.jmoneco.2020.09.003> extension of Gurkaynak,
Sack, and Swanson (2005), the pure monetary policy and central bank
information shocks of Jarocinski and Karadi (2020)
<doi:10.1257/mac.20180090>, the informationally-robust shock of
Miranda-Agrippino and Ricco (2021) <doi:10.1257/mac.20180124>, and the
shadow federal funds rate of Wu and Xia (2016) <doi:10.1111/jmcb.12300>;
for the UK, the UK Monetary Policy Event-Study Database of Braun,
Miranda-Agrippino, and Saha (2025) <doi:10.1016/j.jmoneco.2024.103645>,
the high-frequency surprise of Cesa-Bianchi, Thwaites, and Vicondoa (2020)
<doi:10.1016/j.euroecorev.2020.103375>, and the narrative shock of Cloyne
and Hurtgen (2016) <doi:10.1257/mac.20150093>; for Australia, the
three-component RBA surprise of Hambur and Haque (2023)
<doi:10.1111/1475-4932.12786> and the credit-spread-augmented RBA
narrative shock of Beckers (2020). Helpers support date alignment,
frequency conversion, and shock cumulation. All data is bundled; no
runtime network access is required.

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

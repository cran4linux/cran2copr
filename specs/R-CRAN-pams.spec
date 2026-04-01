%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pams
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Profile Analysis via Multidimensional Scaling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-smacof >= 2.1.0
Requires:         R-CRAN-smacof >= 2.1.0

%description
Implements Profile Analysis via Multidimensional Scaling (PAMS) for the
identification of population-level core response profiles from
cross-sectional and longitudinal person-score data. Each person profile is
decomposed into a level component (the person mean) and a pattern
component (ipsatized subscores). PAMS uses nonmetric multidimensional
scaling via the SMACOF algorithm to identify a small number of core
profiles that represent the central response patterns in a sample of any
size. Bootstrap standard errors and bias-corrected and accelerated (BCa)
confidence intervals for individual core profile coordinates are
estimated, enabling significance testing of coordinates that is not
available in other profile analysis methods such as cluster profile
analysis or latent profile analysis. Person-level weights, R-squared
values, and correlations with core profiles are also estimated, allowing
individual profiles to be interpreted in terms of the core profile
structure. PAMS can be applied to both cross-sectional data and
longitudinal data, where core trajectory profiles describe how response
patterns change over time. Methods are described in Kim and Kim (2024)
<doi:10.20982/tqmp.20.3.p230>, de Leeuw and Mair (2009)
<doi:10.18637/jss.v031.i03>, and Kruskal (1964) <doi:10.1007/BF02289565>.

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

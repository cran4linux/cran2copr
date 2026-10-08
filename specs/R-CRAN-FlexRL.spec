%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FlexRL
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Record Linkage and Linked Data Quality Assessment

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Matrix >= 1.7
BuildRequires:    R-CRAN-Rcpp >= 1.0.13
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BRL 
BuildRequires:    R-CRAN-arf 
BuildRequires:    R-CRAN-diyar 
BuildRequires:    R-CRAN-fastLink 
BuildRequires:    R-CRAN-fedmatch 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-multilink 
BuildRequires:    R-CRAN-reclin2 
BuildRequires:    R-CRAN-synthpop 
Requires:         R-CRAN-Matrix >= 1.7
Requires:         R-CRAN-Rcpp >= 1.0.13
Requires:         R-CRAN-cli 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-BRL 
Requires:         R-CRAN-arf 
Requires:         R-CRAN-diyar 
Requires:         R-CRAN-fastLink 
Requires:         R-CRAN-fedmatch 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-multilink 
Requires:         R-CRAN-reclin2 
Requires:         R-CRAN-synthpop 

%description
Probabilistically link records that refer to the same entities across two
data sources without a unique identifier, using partially identifying
variables such as product code, brand, category, birth year, sex or postal
code. 'FlexRL' implements a Stochastic Expectation Maximisation (StEM)
approach to Record Linkage (Robach et al., 2025,
<doi:10.1093/jrsssc/qlaf016>). The model accounts for registration errors
(missing values and mistakes) and for variables that change over time,
enforces one-to-one assignment, and has a low memory footprint. The
package also provides tools for inference on linked data: two estimators
of the false discovery proportion of a linkage (Robach et al., 2025,
<doi:10.1002/sim.70292>), based on linkage scores and on synthetic data,
and diagnostics comparing the linked sample with the source data. These
tools also apply on the linkage output of other record linkage packages.

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

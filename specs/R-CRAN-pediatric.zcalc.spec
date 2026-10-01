%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pediatric.zcalc
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Z-Score Calculator for Biomarkers: Childhood to Young Adulthood

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-pracma 

%description
Provides tools to compute individual percentile ranks and z-scores for
clinical biomarkers in children, adolescents and young adults, based on
age-, sex-, and height-specific reference data from the IDEFICS
(Identification and prevention of Dietary and lifestyle-induced health
EFfects In Children and infantS) study and the Biomarkers4Pediatrics
collaboration. Supports the computation of a composite Metabolic Syndrome
(MetS) score and associated monitoring/action levels for health
monitoring. For more details see Ahrens et al. (2014)
<doi:10.1038/ijo.2014.130>.

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

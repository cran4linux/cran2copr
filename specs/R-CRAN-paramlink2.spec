%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  paramlink2
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Linkage Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-pedtools 
BuildRequires:    R-CRAN-pedprobr 
Requires:         R-CRAN-pedtools 
Requires:         R-CRAN-pedprobr 

%description
Parametric linkage analysis of monogenic traits in medical pedigrees.
Features include singlepoint analysis, multipoint analysis via 'MERLIN'
(Abecasis et al. (2002) <doi:10.1038/ng786>), visualisation of log of the
odds (LOD) scores and summaries of linkage peaks. Disease models may be
specified to accommodate phenocopies, reduced penetrance and liability
classes. 'paramlink2' is part of the 'ped suite' package ecosystem,
presented in 'Pedigree Analysis in R' (Vigeland, 2021,
ISBN:9780128244302).

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

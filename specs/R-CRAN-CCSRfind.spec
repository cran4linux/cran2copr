%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CCSRfind
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Convert ICD-10 Codes to CCSR Codes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-knitr 

%description
Provides a tool for matching ICD-10 codes to corresponding Clinical
Classification Software Refined (CCSR) codes. The main function,
CCSRfind(), identifies each CCSR code that applies to an individual given
their diagnosis codes. It also provides a summary of CCSR codes that are
matched to a dataset. The package contains 3 datasets: 'DXCCSR' (mapping
of ICD-10 codes to CCSR codes), 'Legend' (conversion of DXCCSR to
CCSRfind-usable format for CCSR codes with less than or equal to 1000
ICD-10 diagnosis codes), and 'LegendExtend' (conversion of DXCCSR to
CCSRfind-usable format for CCSR codes with more than 1000 ICD-10 dx
codes). The disc() function applies grepl() ('base') to multiple columns
and is used in CCSRfind().

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

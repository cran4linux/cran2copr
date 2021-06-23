%global __brp_check_rpaths %{nil}
%global packname  HRM.curve
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          High-Resolution Melting (HRM) Curve Analysis

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch

%description
The analysis of high-resolution melting (HRM) curves provides
cost-efficient post-PCR distinction among amplicons differing by as little
as a single base pair, based on their thermal denaturation (melting)
properties. HRM curve analysis has been used mainly for genotyping and
detection of mutations. Beside genotyping, the method has been used to
differentiate viral, bacterial and fungal pathogens, and it has a
potential for plant genotyping in breeding and as an alternative to DNA
barcoding for taxonomic assignment of species. This package offers
functions that facilitate drawing denaturation, melting, and difference
curves in HRM curve analysis in R. Lukas Beule was supported by the German
Federal Ministry of Education and Research (BMBF) in the framework of the
Bonares-SIGNAL project (funding codes: 031A562A and 031B0510A). Please
cite Schiwek et al. (2020) <doi:10.3390/pathogens9040270> if you use this
package in your work.

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

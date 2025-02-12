%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forrel
%global packver   1.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Forensic Pedigree Analysis and Relatedness Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pedtools >= 2.6.0
BuildRequires:    R-CRAN-ribd >= 1.7.1
BuildRequires:    R-CRAN-pedprobr >= 0.8
BuildRequires:    R-CRAN-verbalisr >= 0.7.1
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-pedtools >= 2.6.0
Requires:         R-CRAN-ribd >= 1.7.1
Requires:         R-CRAN-pedprobr >= 0.8
Requires:         R-CRAN-verbalisr >= 0.7.1
Requires:         R-CRAN-glue 
Requires:         R-CRAN-pbapply 

%description
Forensic applications of pedigree analysis, including likelihood ratios
for relationship testing, general relatedness inference, marker
simulation, and power analysis. 'forrel' is part of the 'pedsuite', a
collection of packages for pedigree analysis, further described in the
book 'Pedigree Analysis in R' (Vigeland, 2021, ISBN:9780128244302).
Several functions deal specifically with power analysis in missing person
cases, implementing methods described in Vigeland et al. (2020)
<doi:10.1016/j.fsigen.2020.102376>. Data import from the 'Familias'
software (Egeland et al. (2000) <doi:10.1016/S0379-0738(00)00147-X>) is
supported through the 'pedFamilias' package.

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

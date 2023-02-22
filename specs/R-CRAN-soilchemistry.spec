%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  soilchemistry
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Properties Related to Soil Chemical Environment and Nutrient Availability

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Facilitates basic and equation-based analyses of some important soil
properties related to soil chemical environment and nutrient availability
to plants. Freundlich H (1907). <doi:10.1515/zpch-1907-5723>. Datta SP,
Bhadoria PBS (1999).
<doi:10.1002%%2F%%28SICI%%291522-2624%%28199903%%29162%%3A2%%3C183%%3A%%3AAID-JPLN183%%3E3.0.CO%%3B2-A>."Boron
adsorption and desorption in some acid soils of West Bengal, India".
Langmuir I (1918). <doi:10.1021/ja02242a004> "The adsorption of gases on
plane surfaces of glass, mica, and platinum". Khasawneh FE (1971).
<doi:10.2136/sssaj1971.03615995003500030029x> "Solution ion activity and
plant growth".

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

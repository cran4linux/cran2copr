%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  biologicalActivityIndices
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Biological Activity Indices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Ecological alteration of degraded lands can improve their sustainability
by addition of large amount of biomass to soil resulting in improved soil
health. Soil biological parameters (such as carbon, nitrogen and
phosphorus cycling enzyme activity) are reactive to minute variations in
soils [Ghosh et al. (2021) <doi:10.1016/j.ecoleng.2021.106176> ]. Hence,
biological activity index combining Urease, Alkaline Phosphatase,
Dehydrogenase (DHA) & Beta-Glucosidase activity will assist in detecting
early changes in restored land use systems [Patidar et al. (2023)
<doi:10.3389/fsufs.2023.1230156>]. This package helps to calculate
Biological Activity Index (BAI) based on vectors of Land Use
System/treatment and control/reference Land Use System containing four
values of Urease, Alkaline Phosphatase, DHA & Beta-Glucosidase. (DHA),
urease (URE), fluorescein diacetate hydrolysis (FDA) and alkaline
phosphatase (ALP) activities are measured in soil samples using triphenyl
tetrazolium chloride, urea, fluorescein diacetate and p-nitro
phenyl-phosphate as substrates, respectively.

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

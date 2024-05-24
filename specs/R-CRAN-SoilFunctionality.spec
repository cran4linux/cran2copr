%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SoilFunctionality
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Soil Functionality Measurement

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Generally, soil functionality is characterized by its capability to
sustain microbial activity, nutritional element supply, structural
stability and aid for crop production. Since soil functions can be linked
to 80%% of ecosystem services, conservation of degraded land should strive
to restore not only the capacity of soil to sustain flora but also
ecosystem provisions. The primary ecosystem services of soil are carbon
sequestration, food or biomass production, provision of microbial habitat,
nutrient recycling. However, the actual magnitude of soil functions
provided by agricultural land uses has never been quantified. Nutrient
supply capacity (NSC) is a measure of nutrient dynamics in restored land
uses. Carbon accumulation proficiency (CAP) is a measure of ecosystem
carbon sequestration. Biological activity index (BAI) is the average of
responses of all enzyme activities in treated land over control/reference
land. The CAP parameter investigates how land uses may affect carbon
flows, retention, and sequestration. The CAP provides a signal for C
cycles, flows, and the systems' relative operational supremacy.

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

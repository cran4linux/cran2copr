%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  okBATHTUB
%global packver   0.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Empirical Reservoir Eutrophication Modelling with Oklahoma Calibration

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Empirical reservoir water quality modelling using Walker's 'BATHTUB' Model
1 (second-order available-phosphorus sedimentation) from Walker (1985)
<https://hdl.handle.net/11681/13884> and Walker (1996)
<https://hdl.handle.net/11681/4353> as the default retention model. The
Vollenweider (1976) hydraulic- residence form and the equivalent
formulation of Larsen and Mercier (1976) are available as alternatives.
Predicts in-lake total phosphorus, total nitrogen, chlorophyll-a, and
Secchi depth from tributary nutrient and hydraulic loading inputs, and
computes Carlson (1977) <doi:10.4319/lo.1977.22.2.0361> Trophic State
Indices. Optional Oklahoma-specific chlorophyll and Secchi regression
coefficients are provided, calibrated from publicly available state lake
monitoring data. Supports single-segment and multi-segment reservoir
configurations and load-reduction scenario analysis. Designed to
complement watershed loading models such as the Soil and Water Assessment
Tool ('SWAT'; <https://swat.tamu.edu>) and the U.S. EPA Hydrologic and
Water Quality System ('HAWQS'; <https://hawqs.tamu.edu>) in a two-model
nutrient management workflow.

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

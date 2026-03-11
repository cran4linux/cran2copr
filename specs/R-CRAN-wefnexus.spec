%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wefnexus
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Water-Energy-Food-Nutrient-Carbon Nexus Analysis for Agronomic Systems

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-rlang 

%description
Provides functions for analysing Water-Energy-Food-Nutrient-Carbon (WEFNC)
nexus interactions in agricultural production systems. Includes functions
for computing water use efficiency (WUE), water productivity (WP), and
water footprint (WF) including green, blue, and grey components following
the methodology of Hoekstra et al. (2011, ISBN:9781849712798). Includes
energy budgeting tools for energy use efficiency (EUE), energy return on
investment (EROI), net energy (NE), and energy productivity (EP). Computes
nutrient use efficiency (NUE) metrics including agronomic efficiency (AE),
physiological efficiency (PE), recovery efficiency (RE), and partial
factor productivity (PFP) as defined by Dobermann (2007)
<https://digitalcommons.unl.edu/agronomyfacpub/316/> and Congreves et al.
(2021) <doi:10.3389/fpls.2021.637108>. Estimates carbon footprint (CF),
greenhouse gas (GHG) emissions, soil organic carbon (SOC) stocks, and
global warming potential (GWP) using Intergovernmental Panel on Climate
Change (IPCC) Sixth Assessment Report (AR6) default values (CH4 = 27, N2O
= 273) as reported in Forster et al. (2021)
<doi:10.1017/9781009157896.009>. Computes composite
Water-Energy-Food-Nutrient-Carbon (WEFNC) nexus indices, trade-off
correlation matrices, and generates radar and heatmap visualizations for
comparing agricultural treatments. Supports conservation agriculture (CA),
irrigated and rain-fed systems, and arid and semi-arid production
environments. Methods follow Lal (2004) <doi:10.1016/j.envint.2004.03.005>
for carbon emissions from farm operations, and Hoover et al. (2023)
<doi:10.1016/j.scitotenv.2022.160992> for water use efficiency indicators.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  whalestrike
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Whale Ship Strikes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-shiny 

%description
Provides tools for simulating the biophysical effects of vessel-strikes on
whales. The aim is to support the evaluation of marine policies limiting
ship speeds through regions in which whales reside. This is important
because ship strikes are a major source of lethality for several whale
species, including the critically endangered North Atlantic right whale.
In this analysis, whales are modelled with a four-layer system comprising
skin, blubber, sub-layer (muscle or organ) and bone. Reasonable values for
the material properties of these layers, along with other factors such as
whale surface area and mass, are provided for a variety of whale species.
Similarly, key values are provided for several ship types.  The collision
is modelled according to Newtonian dynamics, with stresses and strains
within the whale layers being simulated over time. The simulation results
are analyzed in the context of whale-strike data, to develop a Lethality
Index for the whale in the modelled collision.  For the underlying
science, see Kelley and other "Assessing the Lethality of Ship Strikes on
Whales Using Simple Biophysical Models." (2021) <doi:10.1111/mms.12745>.
For more on the R code, see Kelley "`whalestrike`: An R package for
simulating ship strikes on whales" (2024) <doi:10.21105/joss.06473>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SlotLim
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Catch Advice for Fisheries Managed by Harvest Slot Limits

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-patchwork 

%description
Catch advice for data-limited vertebrate and invertebrate fisheries
managed by harvest slot limits using the SlotLim harvest control rule. The
package accompanies the manuscript "SlotLim: catch advice for data-limited
vertebrate and invertebrate fisheries managed by harvest slot limits"
(Pritchard et al., in prep). Minimum data requirements: at least two
consecutive years of catch data, length–frequency distributions, and
biomass or abundance indices (all from fishery-dependent sources);
species-specific growth rate parameters (either von Bertalanffy, Gompertz,
or Schnute); and either the natural mortality rate ('M') or the maximum
observed age ('tmax'), from which M is estimated. The following functions
have optional plotting capabilities that require 'ggplot2' installed:
prop_target(), TBA(), SAM(), catch_advice(), catch_adjust(), and
slotlim_once().

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

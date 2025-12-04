%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SHAKTI
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Suite for Heat-Related Adsorption Knowledge and Thermodynamic Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 

%description
A comprehensive framework for quantifying the fundamental thermodynamic
parameters of adsorption reactions—changes in the standard Gibbs free
energy (delta G), enthalpy (delta H), and entropy (delta S)—is essential
for understanding the spontaneity, heat effects, and molecular ordering
associated with sorption processes. By analysing temperature-dependent
equilibrium data, thermodynamic interpretation expands adsorption studies
beyond conventional isotherm fitting, offering deeper insight into
underlying mechanisms and surface–solute interactions. Such an approach
typically involves evaluating equilibrium coefficients across multiple
temperatures and non-temperature treatments, deriving thermodynamic
parameters using established thermodynamic relationships, and determining
delta G as a temperature-specific indicator of adsorption favourability.
This analytical pathway is widely applicable across environmental science,
soil science, chemistry, materials science, and engineering, where
reliable assessment of sorption behaviour is critical for examining
contaminant retention, nutrient dynamics, and the behaviour of natural and
engineered surfaces. By focusing specifically on thermodynamic inference,
this framework complements existing adsorption isotherm-fitting packages
such as “AdIsMF” <https://CRAN.R-project.org/package=AdIsMF>
<doi:10.32614/CRAN.package.AdIsMF>, and strengthens the scientific basis
for interpreting adsorption energetics in both research and applied
contexts. Details can be found in Roy et al. (2025)
<doi:10.1007/s11270-025-07963-7>.

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

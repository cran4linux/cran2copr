%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rbcmodel
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Model Rubisco Carboxylation Rate Across Temperature, CO2, and O2

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-plot3D 
Requires:         R-CRAN-plot3D 

%description
Collects published kinetics of ribulose 1,5-bisphosphate
carboxylase/oxygenase (Rubisco) and uses these kinetics to model the
carboxylation rate across CO2 and O2 concentrations and different
temperatures. The carboxylation rate can be modeled as the gross rate or
the net rate, which takes into account the oxygenase activity of the
enzyme using one of the three known phosphoglycolate salvage pathways.
Custom enzymes and temperature dependences can be created with user
kinetics, or published kinetics can be accessed through a meta-analysis
contained within the package. An expansion of methods from Harrison et al.
(2025) <doi:10.1128/aem.00604-25>.

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

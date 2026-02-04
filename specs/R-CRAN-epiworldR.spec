%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epiworldR
%global packver   0.11.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Agent-Based Epi Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-methods 

%description
A flexible framework for Agent-Based Models (ABM), the 'epiworldR' package
provides methods for prototyping disease outbreaks and transmission models
using a 'C++' backend, making it very fast. It supports multiple
epidemiological models, including the Susceptible-Infected-Susceptible
(SIS), Susceptible-Infected-Removed (SIR),
Susceptible-Exposed-Infected-Removed (SEIR), and others, involving
arbitrary mitigation policies and multiple-disease models. Users can
specify infectiousness/susceptibility rates as a function of agents'
features, providing great complexity for the model dynamics. Furthermore,
'epiworldR' is ideal for simulation studies featuring large populations.

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

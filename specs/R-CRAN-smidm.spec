%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smidm
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Modelling for Infectious Disease Management

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-extraDistr 
Requires:         R-stats 
Requires:         R-methods 

%description
Statistical models for specific coronavirus disease 2019 use cases at
German local health authorities. All models of Statistical modelling for
infectious disease management 'smidm' are part of the decision support
toolkit in the 'EsteR' project. More information is published in Sonja
Jäckle, Rieke Alpers, Lisa Kühne, Jakob Schumacher, Benjamin Geisler, Max
Westphal "'EsteR' – A Digital Toolkit for COVID-19 Decision Support in
Local Health Authorities" (2022) <doi:10.3233/SHTI220799> and Sonja
Jäckle, Elias Röger, Volker Dicken, Benjamin Geisler, Jakob Schumacher,
Max Westphal "A Statistical Model to Assess Risk for Supporting COVID-19
Quarantine Decisions" (2021) <doi:10.3390/ijerph18179166>.

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

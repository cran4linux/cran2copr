%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Synth
%global packver   1.1-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Synthetic Control Group Method for Comparative Case Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-rgenoud 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-rgenoud 

%description
Implements the synthetic control group method for comparative case studies
as described in Abadie and Gardeazabal (2003) and Abadie, Diamond, and
Hainmueller (2010, 2011, 2014). The synthetic control method allows for
effect estimation in settings where a single unit (a state, country, firm,
etc.) is exposed to an event or intervention. It provides a data-driven
procedure to construct synthetic control units based on a weighted
combination of comparison units that approximates the characteristics of
the unit that is exposed to the intervention. A combination of comparison
units often provides a better comparison for the unit exposed to the
intervention than any comparison unit alone.

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

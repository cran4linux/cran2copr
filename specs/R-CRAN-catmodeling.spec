%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  catmodeling
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Catastrophe Model Simulation and Adjustment

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-geosphere 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-geosphere 

%description
Manipulation of catastrophe model outputs, including tasks such as
simulating year loss tables (YLTs) from event loss tables (ELTs),
adjusting the frequencies of events in YLTs to create new YLTs, applying
catastrophe exceedance of loss contracts (catXL), applying hours clauses,
and calculating diagnostics from ELTs and YLTs, such as average annual
loss and exceedance probability curves. Frequency adjustment routines are
based on the paper "A new simulation algorithm for more precise estimates
of change in catastrophe risk models, with application to hurricanes and
climate change", Jewson, S. (2023); <doi:10.1007/s00477-023-02409-0>. Uses
the compiled language 'Rust' in places and so requires a Rust compiler to
be installed, or a binary installation.

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

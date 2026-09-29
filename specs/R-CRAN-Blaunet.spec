%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Blaunet
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate and Analyze Blau Statuses for Measuring Social Distance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-bslib 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-network 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-bslib 

%description
Calculate and analyze Blau statuses for quantifying social distance
between individuals belonging to organizations. Relational (network) data
can be incorporated for additional analyses. The methods build on
affiliation ecology and Blau space as described by McPherson (1983)
<doi:10.2307/2117719>, McPherson and Ranger-Moore (1991)
<doi:10.1093/sf/70.1.19>, McPherson, Popielarz and Drobnic (1992)
<doi:10.2307/2096202>, McPherson and Rotolo (1996) <doi:10.2307/2096330>,
and McPherson (2004) <doi:10.1093/icc/13.1.263>. The implementation of
Blau-space analyses in 'Blaunet' is described by Genkin et al. (2018)
<doi:10.1371/journal.pone.0204990>. This project is supported by the
Defense Threat Reduction Agency (DTRA) Grant HDTRA-10-1-0043.

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

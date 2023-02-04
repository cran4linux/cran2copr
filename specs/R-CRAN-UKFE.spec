%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  UKFE
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          UK Flood Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-methods 
Requires:         R-CRAN-xml2 
Requires:         R-methods 

%description
Functions to implement the methods of the Flood Estimation Handbook (FEH),
associated updates and the revitalised flood hydrograph model (ReFH).
Currently the package uses NRFA peak flow dataset version 11. Aside from
FEH functionality, further hydrological functions are available. Most of
the methods implemented in this package are described in one or more of
the following: "Flood Estimation Handbook", Centre for Ecology & Hydrology
(1999, ISBN:0 948540 94 X). "Flood Estimation Handbook Supplementary
Report No. 1", Kjeldsen (2007, ISBN:0 903741 15 7). "Regional Frequency
Analysis - an approach based on L-moments", Hosking & Wallis (1997, ISBN:
978 0 521 01940 8). "Proposal of the extreme rank plot for extreme value
analysis: with an emphasis on flood frequency studies", Hammond (2019,
<doi:10.2166/nh.2019.157>). "Making better use of local data in flood
frequency estimation", Environment Agency (2017, ISBN: 978 1 84911 387 8).
"Sampling uncertainty of UK design flood estimation" , Hammond (2021,
<doi:10.2166/nh.2021.059>). "Improving the FEH statistical procedures for
flood frequency estimation", Environment Agency (2008, ISBN: 978 1 84432
920 5). "Low flow estimation in the United Kingdom", Institute of
Hydrology (1992, ISBN 0 948540 45 1). Wallingford HydroSolutions, (2016,
<http://software.hydrosolutions.co.uk/winfap4/Urban-Adjustment-Procedure-Technical-Note.pdf>).
Data from the UK National River Flow Archive (<https://nrfa.ceh.ac.uk/>,
terms and conditions:
<https://nrfa.ceh.ac.uk/costs-terms-and-conditions>).

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

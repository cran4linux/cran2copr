%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metascience
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Catalogue and Shared Infrastructure for Open Metascience Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-tools 
Requires:         R-utils 

%description
Catalogue and shared conventions for a set of independent, interoperable
tools that study research: research indicators, narrative CVs, academic
careers, artificial intelligence use in research, science communication
and the integrity and reproducibility of research outputs. Lists the tools
with their domain, maturity and release status; reports which of them are
installed; validates and normalises persistent identifiers (DOI, 'ORCID'
iD, 'ROR' ID) with their check digits; harmonises the result statuses the
tools use, so that an unverifiable result is never read as a negative one;
writes a machine-readable provenance manifest for any analysis; and offers
a 'Shiny' interface with a section for each installed tool. Every tool
remains usable on its own.

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

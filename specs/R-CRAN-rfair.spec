%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rfair
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Assess the FAIRness of Research Data Objects and Software

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-rvest 
Requires:         R-stats 
Requires:         R-CRAN-stringdist 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-yaml 

%description
A native R implementation of the F-UJI (FAIRsFAIR Research Data Object
Assessment) and FRSM (FAIR for Research Software) metrics for evaluating
how well a research data object or piece of research software satisfies
the FAIR principles (Findable, Accessible, Interoperable, Reusable). The
software metrics operationalize the FAIR Principles for Research Software
(FAIR4RS) of Chue Hong et al. (2022) <doi:10.15497/RDA00068>. Given a
persistent identifier, URL, or code repository, 'rfair' resolves it,
harvests metadata from landing pages and registries, and scores it against
the FAIRsFAIR metrics of Devaraju and Huber (2020)
<doi:10.5281/zenodo.3775793> entirely in R, without requiring an external
assessment server. 'rfair' began as a fork of the 'rfuji' F-UJI API client
and reimplements the assessment engine natively.

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

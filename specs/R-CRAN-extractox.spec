%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  extractox
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extract Tox Info from Various Databases

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-pingr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-webchem 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-pingr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-webchem 
Requires:         R-CRAN-withr 

%description
Extract toxicological and chemical information from databases maintained
by scientific agencies and resources, including the Comparative
Toxicogenomics Database <https://ctdbase.org/>, the Integrated Chemical
Environment <https://ice.ntp.niehs.nih.gov/>, the Integrated Risk
Information System <https://cfpub.epa.gov/ncea/iris/>, Provisional
Peer-Reviewed Toxicity Values
<https://www.epa.gov/pprtv/provisional-peer-reviewed-toxicity-values-pprtvs-assessments>,
the CompTox Chemicals Dashboard Resource Hub
<https://www.epa.gov/comptox-tools/comptox-chemicals-dashboard-resource-hub>,
PubChem <https://pubchem.ncbi.nlm.nih.gov/>, and others.

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

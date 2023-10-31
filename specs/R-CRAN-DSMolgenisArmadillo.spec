%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DSMolgenisArmadillo
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          'DataSHIELD' Client for 'MOLGENIS Armadillo'

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-DSI >= 1.3.0
BuildRequires:    R-CRAN-MolgenisAuth >= 0.0.25
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-urltools 
Requires:         R-CRAN-DSI >= 1.3.0
Requires:         R-CRAN-MolgenisAuth >= 0.0.25
Requires:         R-methods 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-urltools 

%description
'DataSHIELD' is an infrastructure and series of R packages that enables
the remote and 'non-disclosive' analysis of sensitive research data. This
package is the 'DataSHIELD' interface implementation to analyze data
shared on a 'MOLGENIS Armadillo' server. 'MOLGENIS Armadillo' is a
light-weight 'DataSHIELD' server using a file store and an 'RServe'
server.

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

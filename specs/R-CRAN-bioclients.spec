%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bioclients
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Clients for Biological Database Web Services

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-biohttp >= 0.1.2
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-biohttp >= 0.1.2
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-tibble 

%description
Look up genes, variants and proteins from R, without writing a client for
every biological web service. Each service gets one client that makes the
request and returns a table. Parsing is a separate function that needs no
network, so it can run on a saved response and be tested offline.
Transport, retries, caching and error handling are left to the 'biohttp'
package. Dependencies for single services are optional, so you do not
install what you will not use. The services covered include 'Ensembl',
described in Dyer et al. (2025) <doi:10.1093/nar/gkae1071>, 'UniProt', in
The UniProt Consortium (2025) <doi:10.1093/nar/gkae1010>, 'gnomAD', in
Chen et al. (2024) <doi:10.1038/s41586-023-06045-0>, 'Open Targets', in
Buniello et al. (2025) <doi:10.1093/nar/gkae1128>, and the 'AlphaFold'
Protein Structure Database, in Varadi et al. (2024)
<doi:10.1093/nar/gkad1011>. Each client's help page cites the service it
calls.

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

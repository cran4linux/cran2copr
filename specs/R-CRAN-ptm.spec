%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ptm
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyses of Protein Post-Translational Modifications

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bio3d >= 2.3.4
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
Requires:         R-CRAN-bio3d >= 2.3.4
Requires:         R-CRAN-curl 
Requires:         R-graphics 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 

%description
Contains utilities for the analysis of post-translational modifications
(PTMs) in proteins, with particular emphasis on the sulfoxidation of
methionine residues. Features include the ability to download, filter and
analyze data from the sulfoxidation database 'MetOSite'. Utilities to
search and characterize S-aromatic motifs in proteins are also provided.
In addition, functions to analyze sequence environments around modifiable
residues in proteins can be found. For instance, 'ptm' allows to search
for amino acids either overrepresented or avoided around the modifiable
residues from the proteins of interest. Functions tailored to test
statistical hypothesis related to these differential sequence environments
are also implemented. Further and detailed information regarding the
methods in this package can be found in (Aledo (2020)
<https://metositeptm.com>).

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

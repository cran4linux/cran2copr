%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PubMatrixR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          PubMed Pairwise Co-Occurrence Matrix Construction and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-readODS 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-readODS 
Requires:         R-CRAN-xml2 

%description
Queries the 'NCBI' (National Center for Biotechnology Information) Entrez
'E-utilities' API to count pairwise co-occurrences between two sets of
terms in 'PubMed' or 'PubMed Central'. It returns a matrix-like data frame
of publication counts and can export hyperlink-enabled results in CSV or
ODS format. The package also provides heatmap helpers for exploratory
visualization of overlap patterns. Based on the method described in Becker
et al. (2003) "PubMatrix: a tool for multiplex literature mining"
<doi:10.1186/1471-2105-4-61>.

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

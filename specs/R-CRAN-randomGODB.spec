%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  randomGODB
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Random GO Database

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-minimalistGODB 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-minimalistGODB 
Requires:         R-graphics 
Requires:         R-stats 

%description
The Gene Ontology (GO) Consortium <https://geneontology.org/> organizes
genes into hierarchical categories based on biological process (BP),
molecular function (MF) and cellular component (CC, i.e., subcellular
localization). Tools such as 'GoMiner' (see Zeeberg, B.R., Feng, W., Wang,
G. et al. (2003) <doi:10.1186/gb-2003-4-4-r28>) can leverage GO to perform
ontological analysis of microarray and proteomics studies, typically
generating a list of significant functional categories. The significance
is traditionally determined by randomizing the input gene list to
computing the false discovery rate (FDR) of the enrichment p-value for
each category. We explore here the novel alternative of randomizing the GO
database rather than the gene list.

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

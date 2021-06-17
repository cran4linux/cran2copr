%global packname  SignacX
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cell Type Identification and Discovery from Single Cell Gene Expression Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Seurat >= 3.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-igraph >= 1.2.1
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-stats 
Requires:         R-CRAN-Seurat >= 3.2.0
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-igraph >= 1.2.1
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-lme4 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-RJSONIO 
Requires:         R-stats 

%description
An implementation of neural networks trained with flow-sorted gene
expression data to classify cellular phenotypes in single cell
RNA-sequencing data. See Chamberlain M et al. (2021)
<doi:10.1101/2021.02.01.429207> for more details.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

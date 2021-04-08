%global packname  FateID
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantification of Fate Bias in Multipotent Progenitors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lle 
BuildRequires:    R-CRAN-locfit 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-princurve 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-som 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lle 
Requires:         R-CRAN-locfit 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-princurve 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-som 
Requires:         R-stats 
Requires:         R-CRAN-umap 
Requires:         R-utils 

%description
Application of 'FateID' allows computation and visualization of cell fate
bias for multi-lineage single cell transcriptome data. Herman, J.S.,
Sagar, Grün D. (2018) <DOI:10.1038/nmeth.4662>.

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

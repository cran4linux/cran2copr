%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dawnn
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Differential Abundance with Neural Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-tools 
Requires:         R-stats 
Requires:         R-CRAN-Seurat 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-keras 
Requires:         R-utils 
Requires:         R-CRAN-withr 
Requires:         R-tools 

%description
Detects regions of differential abundance in single-cell transcriptomic
data by applying a pre-trained neural network model to the labels of each
cell's nearest neighbours. Tests for both local and global differential
abundance, controlling the false discovery rate with the
Benjamini-Yekutieli procedure. The method is described in Hall and
Castellano (2023) <doi:10.1101/2023.05.05.539427>.

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

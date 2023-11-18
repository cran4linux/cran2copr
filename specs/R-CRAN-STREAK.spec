%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  STREAK
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Receptor Abundance Estimation using Feature Selection and Gene Set Scoring

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Ckmeans.1d.dp 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-CRAN-SPECK 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VAM 
Requires:         R-CRAN-Ckmeans.1d.dp 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Seurat 
Requires:         R-CRAN-SPECK 
Requires:         R-stats 
Requires:         R-CRAN-VAM 

%description
Performs receptor abundance estimation for single cell RNA-sequencing data
using a supervised feature selection mechanism and a thresholded gene set
scoring procedure. Seurat's normalization method is described in: Hao et
al., (2021) <doi:10.1016/j.cell.2021.04.048>, Stuart et al., (2019)
<doi:10.1016/j.cell.2019.05.031>, Butler et al., (2018)
<doi:10.1038/nbt.4096> and Satija et al., (2015) <doi:10.1038/nbt.3192>.
Method for reduced rank reconstruction and rank-k selection is detailed
in: Javaid et al., (2022) <doi:10.1101/2022.10.08.511197>. Gene set
scoring procedure is described in: Frost et al., (2020)
<doi:10.1093/nar/gkaa582>. Clustering method is outlined in: Song et al.,
(2020) <doi:10.1093/bioinformatics/btaa613> and Wang et al., (2011)
<doi:10.32614/RJ-2011-015>.

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

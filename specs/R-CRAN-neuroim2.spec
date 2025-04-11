%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  neuroim2
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Structures for Brain Imaging Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-mmap 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RNifti 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-colorplane 
BuildRequires:    R-CRAN-bigstatsr 
BuildRequires:    R-CRAN-RNiftyReg 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-deflist 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-mmap 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-RNifti 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-stringr 
Requires:         R-methods 
Requires:         R-CRAN-colorplane 
Requires:         R-CRAN-bigstatsr 
Requires:         R-CRAN-RNiftyReg 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-deflist 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 

%description
A collection of data structures and methods for handling volumetric brain
imaging data, with a focus on functional magnetic resonance imaging
(fMRI). Provides efficient representations for three-dimensional and
four-dimensional neuroimaging data through sparse and dense array
implementations, memory-mapped file access for large datasets, and spatial
transformation capabilities. Implements methods for image resampling,
spatial filtering, region of interest analysis, and connected component
labeling. General introduction to fMRI analysis can be found in Poldrack
et al. (2024, "Handbook of functional MRI data analysis",
<ISBN:9781108795760>).

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

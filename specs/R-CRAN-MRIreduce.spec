%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MRIreduce
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          ROI-Based Transformation of Neuroimages into High-Dimensional Data Frames

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-fslr 
BuildRequires:    R-CRAN-neurobase 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-partition 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-fslr 
Requires:         R-CRAN-neurobase 
Requires:         R-CRAN-oro.nifti 
Requires:         R-parallel 
Requires:         R-CRAN-partition 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-reticulate 

%description
Converts NIfTI format T1/FL neuroimages into structured, high-dimensional
2D data frames with a focus on region of interest (ROI) based processing.
The package incorporates the partition algorithm, which offers a flexible
framework for agglomerative partitioning based on the
Direct-Measure-Reduce approach. This method ensures that each reduced
variable maintains a user-specified minimum level of information while
remaining interpretable, as each maps uniquely to one variable in the
reduced dataset. The partition framework is described in Millstein et al.
(2020) <doi:10.1093/bioinformatics/btz661>. The package allows
customization in variable selection, measurement of information loss, and
data reduction methods for neuroimaging analysis and machine learning
workflows.

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

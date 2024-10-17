%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MixfMRI
%global packver   0.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Mixture fMRI Clustering Analysis

License:          Mozilla Public License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-fftw 
BuildRequires:    R-CRAN-MixSim 
BuildRequires:    R-CRAN-EMCluster 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-fftw 
Requires:         R-CRAN-MixSim 
Requires:         R-CRAN-EMCluster 

%description
Utilizing model-based clustering (unsupervised) for functional magnetic
resonance imaging (fMRI) data. The developed methods (Chen and Maitra
(2023) <doi:10.1002/hbm.26425>) include 2D and 3D clustering analyses (for
p-values with voxel locations) and segmentation analyses (for p-values
alone) for fMRI data where p-values indicate significant level of
activation responding to stimulate of interesting. The analyses are mainly
identifying active voxel/signal associated with normal brain behaviors.
Analysis pipelines (R scripts) utilizing this package (see examples in
'inst/workflow/') is also implemented with high performance techniques.

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

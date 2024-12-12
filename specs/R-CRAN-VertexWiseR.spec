%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VertexWiseR
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simplified Vertex-Wise Analyses of Whole-Brain and Hippocampal Surface

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ciftiTools 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-freesurferformats 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-gifti 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-ciftiTools 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-freesurferformats 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-gifti 
Requires:         R-grDevices 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-png 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-reticulate 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Provides functions to run statistical analyses on surface-based
neuroimaging data, computing measures including cortical thickness and
surface area of the whole-brain and of the hippocampi. It can make use of
'FreeSurfer', 'fMRIprep' and 'HCP' preprocessed datasets and 'HippUnfold'
hippocampal segmentation outputs for a given sample by restructuring the
data values into a single file. The single file can then be used by the
package for analyses independently from its base dataset and without need
for its access.

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

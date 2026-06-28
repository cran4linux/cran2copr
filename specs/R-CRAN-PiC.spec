%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PiC
%global packver   3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Processing and Segmentation of Forest TLS Point-Cloud Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-conicfit 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-conicfit 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RANN 
Requires:         R-stats 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-terra 
Requires:         R-tools 
Requires:         R-utils 

%description
Tools for the processing, segmentation, and analysis of terrestrial laser
scanning (TLS and MLS) forest point-cloud data. The package provides fast
voxel-based processing, classification of point clouds into forest floor,
understory, canopy, and woody components, and algorithms for single-tree
analysis and structural characterization. Methods are designed to handle
large and dense point-cloud datasets efficiently, supporting applications
in forest structure assessment, connectivity analysis, and fire-risk
evaluation. Input data are provided as '.xyz', '.txt', '.las', or '.laz'
point-cloud files. For methodological details, see Ferrara and Arrizza
(2025) <https://hdl.handle.net/20.500.14243/533471> and Ferrara et al.
(2018) <doi:10.1016/j.agrformet.2018.04.008>.

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

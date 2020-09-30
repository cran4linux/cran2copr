%global packname  brainGraph
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Graph Theory Analysis of Brain MRI Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 1.2.4
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-grid 
BuildRequires:    R-lattice 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-parallel 
Requires:         R-CRAN-igraph >= 1.2.4
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-CRAN-abind 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-grid 
Requires:         R-lattice 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-permute 
Requires:         R-parallel 

%description
A set of tools for performing graph theory analysis of brain MRI data. It
works with data from a Freesurfer analysis (cortical thickness, volumes,
local gyrification index, surface area), diffusion tensor tractography
data (e.g., from FSL) and resting-state fMRI data (e.g., from DPABI). It
contains a graphical user interface for graph visualization and data
exploration, along with several functions for generating useful figures.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

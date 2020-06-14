%global packname  brainGraph
%global packver   2.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.3
Release:          2%{?dist}
Summary:          Graph Theory Analysis of Brain MRI Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-CRAN-abind 
Requires:         R-CRAN-ade4 
Requires:         R-boot 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Hmisc 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-permute 
Requires:         R-parallel 
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-scales 

%description
A set of tools for performing graph theory analysis of brain MRI data. It
works with data from a Freesurfer analysis (cortical thickness, volumes,
local gyrification index, surface area), diffusion tensor tractography
data (e.g., from FSL) and resting-state fMRI data (e.g., from DPABI). It
contains a graphical user interface for graph visualization and data
exploration, along with several functions for generating useful figures.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

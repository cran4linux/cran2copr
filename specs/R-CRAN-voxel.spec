%global __brp_check_rpaths %{nil}
%global packname  voxel
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          3%{?dist}%{?buildtag}
Summary:          Mass-Univariate Voxelwise Analysis of Medical Imaging Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-lmerTest >= 3.0.1
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-gamm4 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-lmerTest >= 3.0.1
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-mgcv 
Requires:         R-CRAN-gamm4 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-purrr 

%description
Functions for the mass-univariate voxelwise analysis of medical imaging
data that follows the NIfTI <http://nifti.nimh.nih.gov> format.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

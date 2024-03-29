%global __brp_check_rpaths %{nil}
%global packname  cryst
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Calculate the Relative Crystallinity of Starch by XRD and FTIR

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-flux 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
Requires:         R-CRAN-flux 
Requires:         R-CRAN-pracma 
Requires:         R-stats 

%description
Functions to calculate the relative crystallinity of starch by X-ray
Diffraction (XRD) and Infrared Spectroscopy (FTIR). Starch is
biosynthesized by plants in the form of granules semicrystalline. For XRD,
the relative crystallinity is obtained by separating the crystalline peaks
from the amorphous scattering region. For FTIR, the relative crystallinity
is achieved by setting of a Gaussian holocrystalline-peak in the 800-1300
cm-1 region of FTIR spectrum of starch which is divided into amorphous
region and crystalline region. The relative crystallinity of native starch
granules varies from 14 of 45 percent. This package was supported by
FONDECYT 3150630 and CIPA Conicyt-Regional R08C1002 is gratefully
acknowledged.

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

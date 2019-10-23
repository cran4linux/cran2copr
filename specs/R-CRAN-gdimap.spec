%global packname  gdimap
%global packver   0.1-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}
Summary:          Generalized Diffusion Magnetic Resonance Imaging

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-movMF 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-movMF 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-abind 

%description
Diffusion anisotropy has been used to characterize white matter neuronal
pathways in the human brain, and infer global connectivity in the central
nervous system. The package implements algorithms to estimate and
visualize the orientation of neuronal pathways in model-free methods
(q-space imaging methods). For estimating fibre orientations two methods
have been implemented.  One method implements fibre orientation detection
through local maxima extraction. A second more robust method is based on
directional statistical clustering of ODF voxel data. Fibre orientations
in multiple fibre voxels are estimated using a mixture of von Mises-Fisher
(vMF) distributions. This statistical estimation procedure is used to
resolve crossing fibre configurations. Reconstruction of orientation
distribution function (ODF) profiles may be performed using the standard
generalized q-sampling imaging (GQI) approach, Garyfallidis' GQI (GQI2)
approach, or Aganj's variant of the Q-ball imaging (CSA-QBI) approach.
Procedures for the visualization of RGB-maps, line-maps and glyph-maps of
real diffusion magnetic resonance imaging (dMRI) data-sets are included in
the package.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

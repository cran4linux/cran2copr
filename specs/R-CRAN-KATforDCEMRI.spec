%global packname  KATforDCEMRI
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Kinetic Analysis and Visualization of DCE-MRI Data

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.0
Requires:         R-core >= 2.11.0
BuildArch:        noarch
BuildRequires:    R-CRAN-locfit 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-matlab 
Requires:         R-CRAN-locfit 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-matlab 

%description
Provides kinetic analysis of Dynamic Contrast Enhanced Magnetic Resonance
Imaging (DCE-MRI) data. Includes tools for fitting the Tofts (described in
Tofts, Kermode (1991) <DOI:10.1002/mrm.1910170208>) and extended Tofts
(described in Tofts et al. (1999)
<https://www.ncbi.nlm.nih.gov/pubmed/10508281>) mathematical models to
dynamic (signal vs. time) data associated with each voxel of an image and
a Graphical User Inferface (GUI) for visualization and exploration of
fitted model parameters over the volume of the image.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

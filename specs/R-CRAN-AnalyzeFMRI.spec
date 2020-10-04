%global packname  AnalyzeFMRI
%global packver   1.1-21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.21
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Analysis of fMRI Datasets Stored in the ANALYZE orNIFTI Format

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-fastICA 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkrplot 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-fastICA 
Requires:         R-tcltk 
Requires:         R-CRAN-tkrplot 

%description
Functions for I/O, visualisation and analysis of functional Magnetic
Resonance Imaging (fMRI) datasets stored in the ANALYZE or NIFTI format.
Note that the latest version of XQuartz seems to be necessary under MacOS.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AnalyzeFMRI.gui.R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/example-nifti.hdr
%doc %{rlibdir}/%{packname}/example-nifti.img
%doc %{rlibdir}/%{packname}/example.hdr
%doc %{rlibdir}/%{packname}/example.img
%doc %{rlibdir}/%{packname}/example.mat
%doc %{rlibdir}/%{packname}/GRF.examples.R
%doc %{rlibdir}/%{packname}/HISTORY
%doc %{rlibdir}/%{packname}/ICA.gui.R
%doc %{rlibdir}/%{packname}/ICAst.gui.R
%doc %{rlibdir}/%{packname}/niftidoc
%doc %{rlibdir}/%{packname}/plot.volume.gui.R
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/README.win
%doc %{rlibdir}/%{packname}/smoothing.examples.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

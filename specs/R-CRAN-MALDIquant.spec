%global packname  MALDIquant
%global packver   1.19.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.19.3
Release:          1%{?dist}
Summary:          Quantitative Analysis of Mass Spectrometry Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-methods 
Requires:         R-parallel 

%description
A complete analysis pipeline for matrix-assisted laser
desorption/ionization-time-of-flight (MALDI-TOF) and other two-dimensional
mass spectrometry data. In addition to commonly used plotting and
processing methods it includes distinctive features, namely baseline
subtraction methods such as morphological filters (TopHat) or the
statistics-sensitive non-linear iterative peak-clipping algorithm (SNIP),
peak alignment using warping functions, handling of replicated
measurements as well as allowing spectra with different resolutions.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

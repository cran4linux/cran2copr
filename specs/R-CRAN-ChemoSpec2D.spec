%global packname  ChemoSpec2D
%global packver   0.4.147
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.147
Release:          2%{?dist}
Summary:          Exploratory Chemometrics for 2D Spectroscopy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ChemoSpecUtils >= 0.3
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-readJDX 
Requires:         R-CRAN-ChemoSpecUtils >= 0.3
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-readJDX 

%description
A collection of functions for exploratory chemometrics of 2D spectroscopic
data sets such as COSY (correlated spectroscopy) and HSQC (heteronuclear
single quantum coherence) 2D NMR (nuclear magnetic resonance) spectra.
'ChemoSpec2D' deploys methods aimed primarily at classification of samples
and the identification of spectral features which are important in
distinguishing samples from each other. Each 2D spectrum (a matrix) is
treated as the unit of observation, and thus the physical sample in the
spectrometer corresponds to the sample from a statistical perspective.  In
addition to chemometric tools, a few tools are provided for plotting 2D
spectra, but these are not intended to replace the functionality typically
available on the spectrometer. 'ChemoSpec2D' takes many of its cues from
'ChemoSpec' and tries to create consistent graphical output and to be very
user friendly.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX

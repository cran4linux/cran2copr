%global packname  spftir
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Pre-Processing and Analysis of Mid-Infrared Spectral Region

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
Requires:         R-CRAN-pracma 
Requires:         R-stats 

%description
Functions to manipulate, pre-process and analyze spectra in the
mid-infrared region. The pre-processing of the mid-infrared spectra is a
transcendental step in the spectral analysis. Preprocessing of the spectra
includes smoothing, offset, baseline correction, and normalization, is
performed before the analysis of the spectra and is essential to obtain
conclusive results in subsequent quantitative or qualitative analysis.
This package was supported by FONDECYT 3150630, and CIPA Conicyt-Regional
R08C1002 is gratefully acknowledged.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

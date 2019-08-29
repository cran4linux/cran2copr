%global packname  EMD
%global packver   1.5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.8
Release:          1%{?dist}
Summary:          Empirical Mode Decomposition and Hilbert Spectral Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-fields >= 6.9.1
BuildRequires:    R-CRAN-locfit >= 1.5.8
Requires:         R-CRAN-fields >= 6.9.1
Requires:         R-CRAN-locfit >= 1.5.8

%description
For multiscale analysis, this package carries out empirical mode
decomposition and Hilbert spectral analysis. For usage of EMD, see Kim and
Oh, 2009 (Kim, D and Oh, H.-S. (2009) EMD: A Package for Empirical Mode
Decomposition and Hilbert Spectrum, The R Journal, 1, 40-46).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

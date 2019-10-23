%global packname  hht
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}
Summary:          The Hilbert-Huang Transform: Tools and Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 6.7
BuildRequires:    R-CRAN-EMD >= 1.5.5
BuildRequires:    R-CRAN-spatstat >= 1.38.1
Requires:         R-CRAN-fields >= 6.7
Requires:         R-CRAN-EMD >= 1.5.5
Requires:         R-CRAN-spatstat >= 1.38.1

%description
Builds on the EMD package to provide additional tools for empirical mode
decomposition (EMD) and Hilbert spectral analysis. It also implements the
ensemble empirical decomposition (EEMD) and the complete ensemble
empirical mode decomposition (CEEMD) methods to avoid mode mixing and
intermittency problems found in EMD analysis.  The package comes with
several plotting methods that can be used to view intrinsic mode
functions, the HHT spectrum, and the Fourier spectrum.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX

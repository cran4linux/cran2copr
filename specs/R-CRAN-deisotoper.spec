%global debug_package %{nil}
%global packname  deisotoper
%global packver   0.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          1%{?dist}
Summary:          Detection of Isotope Pattern of a Mass Spectrometric Measurement

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-rJava >= 0.9
Requires:         R-CRAN-rJava >= 0.9

%description
Provides a low-level interface for a deisotoper container implemented in
the 'Java' programming language and means of S3 helper functions for
plotting and debugging isotopes of mass spectrometric data. The deisotoper
algorithm detects and aggregates peaks which belong to the same isotopic
cluster of a given mass spectrum.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/dot
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX

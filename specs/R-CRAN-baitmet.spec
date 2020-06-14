%global packname  baitmet
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Library Driven Compound Profiling in Gas Chromatography - MassSpectrometry Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-erah >= 1.0.5
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-HiClimR 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-methods 
Requires:         R-CRAN-erah >= 1.0.5
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-HiClimR 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-signal 
Requires:         R-methods 

%description
Automated quantification of metabolites by targeting mass
spectral/retention time libraries into full scan-acquired gas
chromatography - mass spectrometry (GC-MS) chromatograms. Baitmet outputs
a table with compounds name, spectral matching score, retention index
error, and compounds area in each sample. Baitmet can automatically
determine the compounds retention indexes with or without co-injection of
internal standards with samples.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

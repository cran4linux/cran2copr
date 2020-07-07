%global packname  CepLDA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Discriminant Analysis of Time Series in the Presence ofWithin-Group Spectral Variability

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-astsa 
BuildRequires:    R-MASS 
BuildRequires:    R-class 
BuildRequires:    R-CRAN-multitaper 
Requires:         R-CRAN-astsa 
Requires:         R-MASS 
Requires:         R-class 
Requires:         R-CRAN-multitaper 

%description
Performs cepstral based discriminant analysis of groups of time series
when there exists Variability in power spectra from time series within the
same group as described in R.T. Krafty (2016) "Discriminant Analysis of
Time Series in the Presence of Within-Group Spectral Variability" Journal
of Time Series Analysis.

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
%{rlibdir}/%{packname}/INDEX

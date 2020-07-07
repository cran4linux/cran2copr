%global packname  RHRV
%global packver   4.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.5
Release:          3%{?dist}
Summary:          Heart Rate Variability Analysis of ECG Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-tcltk >= 2.4.1
BuildRequires:    R-CRAN-waveslim >= 1.6.4
BuildRequires:    R-CRAN-lomb >= 1.0
BuildRequires:    R-CRAN-nonlinearTseries >= 0.2.3
BuildRequires:    R-CRAN-tkrplot >= 0.0.18
Requires:         R-tcltk >= 2.4.1
Requires:         R-CRAN-waveslim >= 1.6.4
Requires:         R-CRAN-lomb >= 1.0
Requires:         R-CRAN-nonlinearTseries >= 0.2.3
Requires:         R-CRAN-tkrplot >= 0.0.18

%description
Allows users to import data files containing heartbeat positions in the
most broadly used formats, to remove outliers or points with unacceptable
physiological values present in the time series, to plot HRV data, and to
perform time domain, frequency domain and nonlinear HRV analysis. See
Garcia et al. (2017) <DOI:10.1007/978-3-319-65355-6>.

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
%doc %{rlibdir}/%{packname}/COPYRIGHT
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

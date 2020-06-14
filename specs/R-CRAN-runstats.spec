%global packname  runstats
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Fast Computation of Running Statistics for Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fftwtools 
Requires:         R-CRAN-fftwtools 

%description
Provides methods for fast computation of running sample statistics for
time series. These include: (1) mean, (2) standard deviation, and (3)
variance over a fixed-length window of time-series, (4) correlation, (5)
covariance, and (6) Euclidean distance (L2 norm) between short-time
pattern and time-series. Implemented methods utilize Convolution Theorem
to compute convolutions via Fast Fourier Transform (FFT).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/benchmark_results
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

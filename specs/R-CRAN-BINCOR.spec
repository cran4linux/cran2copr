%global packname  BINCOR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Estimate the Correlation Between Two Irregular Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-pracma 

%description
Estimate the correlation between two irregular time series that are not
necessarily sampled on identical time points. This program is also
applicable to the situation of two evenly spaced time series that are not
on the same time grid. 'BINCOR' is based on a novel estimation approach
proposed by Mudelsee (2010, 2014) to estimate the correlation between two
climate time series with different timescales. The idea is that
autocorrelation (AR1 process) allows to correlate values obtained on
different time points. 'BINCOR' contains four functions: bin_cor() (the
main function to build the binned time series), plot_ts() (to plot and
compare the irregular and binned time series, cor_ts() (to estimate the
correlation between the binned time series) and ccf_ts() (to estimate the
cross-correlation between the binned time series).

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX

%global packname  sazedR
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}
Summary:          Parameter-Free Domain-Agnostic Season Length Detection in TimeSeries

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma >= 2.1.4
BuildRequires:    R-CRAN-zoo >= 1.8.3
BuildRequires:    R-CRAN-bspec >= 1.5
BuildRequires:    R-CRAN-fftwtools >= 0.9.8
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-pracma >= 2.1.4
Requires:         R-CRAN-zoo >= 1.8.3
Requires:         R-CRAN-bspec >= 1.5
Requires:         R-CRAN-fftwtools >= 0.9.8
Requires:         R-CRAN-dplyr >= 0.8.0.1

%description
Spectral and Average Autocorrelation Zero Distance Density ('sazed') is a
method for estimating the season length of a seasonal time series. 'sazed'
is aimed at practitioners, as it employs only domain-agnostic
preprocessing and does not depend on parameter tuning or empirical
constants. The computation of 'sazed' relies on the efficient
autocorrelation computation methods suggested by Thibauld Nion (2012, URL:
<http://www.tibonihoo.net/literate_musing/autocorrelations.html>) and by
Bob Carpenter (2012, URL:
<https://lingpipe-blog.com/2012/06/08/autocorrelation-fft-kiss-eigen/>).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX

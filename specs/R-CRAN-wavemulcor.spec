%global packname  wavemulcor
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}
Summary:          Wavelet Routines for Global and Local Multiple Correlation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-waveslim >= 1.7.5
Requires:         R-CRAN-waveslim >= 1.7.5

%description
Wavelet routines that calculate single sets of wavelet multiple
correlations (WMC) and cross-correlations (WMCC) out of n variables. They
can later be plotted in single graphs, as an alternative to trying to make
sense out of several sets of wavelet correlations or wavelet
cross-correlations. The code is based on the calculation, at each wavelet
scale, of the square root of the coefficient of determination in a linear
combination of variables for which such coefficient of determination is a
maximum. The code provided here is based on the wave.correlation routine
in Brandon Whitcher's waveslim R package Version: 1.6.4, which in turn is
based on wavelet methodology developed in Percival and Walden (2000)
<DOI:10.1017/CBO9780511841040>; Gençay, Selçuk and Whitcher (2002)
<DOI:10.1016/B978-012279670-8.50013-6> and others. Version 2 incorporates
wavelet local multiple correlations (WLMC). These are like the previous
global WMC but consisting in one single set of multiscale correlations
along time. That is, at each time t, they are calculated by letting a
window of weighted wavelet coefficients around t move along time. Six
weight functions are provided. Namely, the uniform window, Cleveland's
tricube window, Epanechnikov's parabolic window, Bartlett's triangular
window and Wendland's truncated power window and the Gaussian window.
Version 2.2 incorporates an auxiliary function that calculates local
multiple correlations (LMC). They are calculated by letting move along
time a window of weighted time series values around t. Any of the six
weight functions mentioned above can be used.

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
%{rlibdir}/%{packname}/INDEX

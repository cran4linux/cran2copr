%global packname  waveband
%global packver   4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.7
Release:          1%{?dist}
Summary:          Computes Credible Intervals for Bayesian Wavelet Shrinkage

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildRequires:    R-CRAN-wavethresh >= 4.6
Requires:         R-CRAN-wavethresh >= 4.6

%description
Computes Bayesian wavelet shrinkage credible intervals for nonparametric
regression. The method uses cumulants to derive Bayesian credible
intervals for wavelet regression estimates. The first four cumulants of
the posterior distribution of the estimates are expressed in terms of the
observed data and integer powers of the mother wavelet functions. These
powers are closely approximated by linear combinations of wavelet scaling
functions at an appropriate finer scale. Hence, a suitable modification of
the discrete wavelet transform allows the posterior cumulants to be found
efficiently for any data set. Johnson transformations then yield the
credible intervals themselves. Barber, S., Nason, G.P. and Silverman, B.W.
(2002) <doi:10.1111/1467-9868.00332>.

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
%doc %{rlibdir}/%{packname}/CHANGES
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

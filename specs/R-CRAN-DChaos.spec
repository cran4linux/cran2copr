%global packname  DChaos
%global packver   0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Chaotic Time Series Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-outliers 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-NeuralNetTools 
BuildRequires:    R-CRAN-entropy 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-outliers 
Requires:         R-nnet 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-NeuralNetTools 
Requires:         R-CRAN-entropy 

%description
Provides several algorithms for the purpose of detecting chaotic signals
inside univariate time series. We focus on methods derived from chaos
theory which estimate the complexity of a dataset through exploring the
structure of the attractor. We have taken into account the Lyapunov
exponents as an ergodic measure. We have implemented the Jacobian method
by a fit through neural networks in order to estimate both the largest and
the spectrum of Lyapunov exponents. We have considered the full sample and
three different methods of subsampling by blocks (non-overlapping, equally
spaced and bootstrap) to estimate them. In addition, it is possible to
make inference about them and know if the estimated Lyapunov exponents
values are or not statistically significant. This library can be used with
time series whose time-lapse is fixed or variable. That is, it considers
time series whose observations are sampled at fixed or variable time
intervals. For a review see David Ruelle and Floris Takens (1971)
<doi:10.1007/BF01646553>, Ramazan Gencay and W. Davis Dechert (1992)
<doi:10.1016/0167-2789(92)90210-E>, Jean-Pierre Eckmann and David Ruelle
(1995) <doi:10.1103/RevModPhys.57.617>, Mototsugu Shintani and Oliver
Linton (2004) <doi:10.1016/S0304-4076(03)00205-7>, Jeremy P. Huke and
David S. Broomhead (2007) <doi:10.1088/0951-7715/20/9/011>.

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

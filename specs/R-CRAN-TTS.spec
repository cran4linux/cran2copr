%global packname  TTS
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Master Curve Estimates Corresponding to Time-TemperatureSuperposition

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-splines 
Requires:         R-mgcv 
Requires:         R-CRAN-sfsmisc 
Requires:         R-splines 

%description
Time-Temperature Superposition analysis is often applied to frequency
modulated data obtained by Dynamic Mechanic Analysis (DMA) and Rheometry
in the analytical chemistry and physics areas. These techniques provide
estimates of material mechanical properties (such as moduli) at different
temperatures in a wider range of time. This package provides the
Time-Temperature superposition Master Curve at a referred temperature by
the three methods: the two wider used methods, Arrhenius based methods and
WLF, and the newer methodology based on derivatives procedure. The Master
Curve is smoothed by B-splines basis. The package output is composed of
plots of experimental data, horizontal and vertical shifts, TTS data, and
TTS data fitted using B-splines with bootstrap confidence intervals.

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
%{rlibdir}/%{packname}/INDEX

%global packname  PRSim
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Stochastic Simulation of Streamflow Time Series using PhaseRandomization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-homtest 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-stats 
Requires:         R-CRAN-homtest 
Requires:         R-CRAN-goftest 
Requires:         R-stats 

%description
Provides a simulation framework to simulate streamflow time series with
similar main characteristics as observed data. These characteristics
include the distribution of daily streamflow values and their temporal
correlation as expressed by short- and long-range dependence. The approach
is based on the randomization of the phases of the Fourier transform. We
further use the flexible four-parameter Kappa distribution, which allows
for the extrapolation to yet unobserved low and high flows. Alternatively,
the empirical or any other distribution can be used. A detailed
description of the simulation approach and an application example can be
found in <https://www.hydrol-earth-syst-sci-discuss.net/hess-2019-142/>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

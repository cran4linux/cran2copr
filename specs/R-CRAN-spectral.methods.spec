%global packname  spectral.methods
%global packver   0.7.2.133
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2.133
Release:          1%{?dist}
Summary:          Singular Spectrum Analysis (SSA) Tools for Time Series Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rssa >= 0.11
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-RNetCDF 
BuildRequires:    R-CRAN-ncdf.tools 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-JBTools 
BuildRequires:    R-CRAN-DistributionUtils 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rssa >= 0.11
Requires:         R-CRAN-raster 
Requires:         R-nnet 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-RNetCDF 
Requires:         R-CRAN-ncdf.tools 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-JBTools 
Requires:         R-CRAN-DistributionUtils 
Requires:         R-CRAN-RColorBrewer 

%description
Contains some implementations of Singular Spectrum Analysis (SSA) for the
gapfilling and spectral decomposition of time series. It contains the code
used by Buttlar et. al. (2014), Nonlinear Processes in Geophysics. In
addition, the iterative SSA gapfilling method of Kondrashov and Ghil
(2006) is implemented. All SSA calculations are done via the truncated and
fast SSA algorithm of Korobeynikov (2010) (package 'Rssa').

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

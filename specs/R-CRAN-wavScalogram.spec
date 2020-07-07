%global packname  wavScalogram
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Wavelet Scalogram Tools for Time Series Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-fields 
Requires:         R-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-zoo 

%description
Provides scalogram based wavelet tools for time series analysis: wavelet
power spectrum, scalogram, windowed scalogram, windowed scalogram
difference (see Bolos et al. (2017) <doi:10.1016/j.amc.2017.05.046>),
scale index and windowed scale index (Benitez et al. (2010)
<doi:10.1016/j.camwa.2010.05.010>).

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

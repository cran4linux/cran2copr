%global packname  WaveletGARCH
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Fit the Wavelet-GARCH Model to Volatile Time Series Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-wavelets 
BuildRequires:    R-CRAN-FinTS 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-CRAN-fracdiff 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-wavelets 
Requires:         R-CRAN-FinTS 
Requires:         R-CRAN-forecast 
Requires:         R-parallel 
Requires:         R-CRAN-rugarch 
Requires:         R-CRAN-fracdiff 
Requires:         R-methods 

%description
Fits the combination of Wavelet-GARCH model for time series forecasting
using algorithm by Paul (2015) <doi:10.3233/MAS-150328>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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

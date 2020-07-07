%global packname  freqdom
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}
Summary:          Frequency Domain Based Analysis: Dynamic PCA

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-base 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-base 
Requires:         R-CRAN-matrixcalc 
Requires:         R-utils 

%description
Implementation of dynamic principal component analysis (DPCA), simulation
of VAR and VMA processes and frequency domain tools. These frequency
domain methods for dimensionality reduction of multivariate time series
were introduced by David Brillinger in his book Time Series (1974). We
follow implementation guidelines as described in Hormann, Kidzinski and
Hallin (2016), Dynamic Functional Principal Component
<doi:10.1111/rssb.12076>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

%global packname  ArfimaMLM
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Arfima-MLM Estimation For Repeated Cross-Sectional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-fractal 
BuildRequires:    R-CRAN-fracdiff 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-fractal 
Requires:         R-CRAN-fracdiff 

%description
Functions to facilitate the estimation of Arfima-MLM models for repeated
cross-sectional data and pooled cross-sectional time-series data (see Lebo
and Weber 2015). The estimation procedure uses double filtering with
Arfima methods to account for autocorrelation in repeated cross-sectional
data followed by multilevel modeling (MLM) to estimate aggregate as well
as individual-level parameters simultaneously.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

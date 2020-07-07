%global packname  TSrepr
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}
Summary:          Time Series Representations

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-wavelets 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-dtt 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-MASS 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-wavelets 
Requires:         R-mgcv 
Requires:         R-CRAN-dtt 

%description
Methods for representations (i.e. dimensionality reduction, preprocessing,
feature extraction) of time series to help more accurate and effective
time series data mining. Non-data adaptive, data adaptive, model-based and
data dictated (clipped) representation methods are implemented. Also
min-max and z-score normalisations, and forecasting accuracy measures are
implemented.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

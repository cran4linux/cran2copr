%global packname  wavemulcor
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          2%{?dist}
Summary:          Wavelet Routines for Global and Local Multiple Regression andCorrelation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-waveslim >= 1.7.5
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-waveslim >= 1.7.5
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-RColorBrewer 

%description
Wavelet routines that calculate single sets of wavelet multiple
regressions and correlations, and cross-regressions and cross-correlations
from a multivariate time series. Dynamic versions of the routines allow
the wavelet local multiple (cross-)regressions and (cross-)correlations to
evolve over time.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

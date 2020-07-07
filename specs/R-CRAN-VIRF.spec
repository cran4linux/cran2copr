%global packname  VIRF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Computation of Volatility Impulse Response Function ofMultivariate Time Series

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rmgarch 
BuildRequires:    R-CRAN-mgarchBEKK 
BuildRequires:    R-CRAN-gnm 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-BigVAR 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-matlib 
Requires:         R-stats 
Requires:         R-CRAN-rmgarch 
Requires:         R-CRAN-mgarchBEKK 
Requires:         R-CRAN-gnm 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-BigVAR 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-matlib 

%description
Computation of volatility impulse response function for multivariate time
series model using algorithm by Jin, Lin and Tamvakis (2012)
<doi.org/10.1016/j.eneco.2012.03.003>.

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

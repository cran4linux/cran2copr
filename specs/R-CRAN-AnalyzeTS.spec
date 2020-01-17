%global packname  AnalyzeTS
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          1%{?dist}
Summary:          Analyze Fuzzy Time Series

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-TSA 
BuildRequires:    R-CRAN-TTR 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-urca 
Requires:         R-MASS 
Requires:         R-CRAN-TSA 
Requires:         R-CRAN-TTR 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-urca 

%description
Analyze fuzzy time series by Chen (1996), Singh (2008), Heuristic (Huarng
2001) and Chen-Hsu (2004) models. The Abbasov - Manedova (2010) and NFTS
models is included as well.

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

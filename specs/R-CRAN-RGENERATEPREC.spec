%global packname  RGENERATEPREC
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Tools to Generate Daily-Precipitation Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-RGENERATE 
BuildRequires:    R-CRAN-blockmatrix 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RMAWGEN 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-RGENERATE 
Requires:         R-CRAN-blockmatrix 
Requires:         R-Matrix 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RMAWGEN 

%description
The method 'generate()' is extended for spatial multi-site stochastic
generation of daily precipitation. It generates precipitation occurrence
in several sites using logit regression (Generalized Linear Models) and
D.S. Wilks' approach (Journal of Hydrology, 1998).

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
%doc %{rlibdir}/%{packname}/example.generate.R
%doc %{rlibdir}/%{packname}/example.wilks1998_second.R
%doc %{rlibdir}/%{packname}/example.wilks1998.R
%doc %{rlibdir}/%{packname}/precipitation_generator
%doc %{rlibdir}/%{packname}/README
%{rlibdir}/%{packname}/INDEX

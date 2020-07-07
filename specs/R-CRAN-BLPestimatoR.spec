%global packname  BLPestimatoR
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}
Summary:          Performs a BLP Demand Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-mvQuad 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-mvQuad 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-Formula 
Requires:         R-stats 
Requires:         R-Matrix 

%description
Provides the estimation algorithm to perform the demand estimation
described in Berry, Levinsohn and Pakes (1995) <DOI:10.2307/2171802> . The
routine uses analytic gradients and offers a large number of implemented
integration methods and optimization routines.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

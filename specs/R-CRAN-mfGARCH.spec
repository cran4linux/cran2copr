%global packname  mfGARCH
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}
Summary:          Mixed-Frequency GARCH Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-maxLik 
Requires:         R-CRAN-Rcpp 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-maxLik 

%description
Estimating GARCH-MIDAS (MIxed-DAta-Sampling) models (Engle, Ghysels, Sohn,
2013, <doi:10.1162/REST_a_00300>) and related statistical inference,
accompanying the paper "Two are better than one: volatility forecasting
using multiplicative component GARCH models" by Conrad and Kleen (2018,
<doi:10.2139/ssrn.2752354>). The GARCH-MIDAS model decomposes the
conditional variance of (daily) stock returns into a short- and long-term
component, where the latter may depend on an exogenous covariate sampled
at a lower frequency.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

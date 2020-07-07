%global packname  ivx
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Robust Econometric Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.300.2.0
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
Drawing statistical inference on the coefficients of a short- or
long-horizon predictive regression with persistent regressors by using the
IVX method of Magdalinos and Phillips (2009) and
<doi:10.1017/S0266466608090154> Kostakis, Magdalinos and Stamatogiannis
(2015) <doi:10.1093/rfs/hhu139>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

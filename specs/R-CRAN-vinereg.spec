%global packname  vinereg
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          4%{?dist}
Summary:          D-Vine Quantile Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-kde1d >= 1.0.2
BuildRequires:    R-CRAN-rvinecopulib >= 0.5.0.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-wdm 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-kde1d >= 1.0.2
Requires:         R-CRAN-rvinecopulib >= 0.5.0.1.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-assertthat 

%description
Implements D-vine quantile regression models with parametric or
nonparametric pair-copulas. See Kraus and Czado (2017)
<doi:10.1016/j.csda.2016.12.009> and Schallhorn et al. (2017)
<arXiv:1705.08310>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

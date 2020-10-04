%global packname  mumm
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Multiplicative Mixed Models using the Template Model Builder

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-Rcpp 
Requires:         R-Matrix 
Requires:         R-CRAN-stringr 
Requires:         R-methods 

%description
Fit multiplicative mixed models using maximum likelihood estimation via
the Template Model Builder (TMB), Kristensen K, Nielsen A, Berg CW, Skaug
H, Bell BM (2016) <doi:10.18637/jss.v070.i05>. One version of the
multiplicative mixed model is applied in Piepho (1999)
<doi:10.1111/j.0006-341X.1999.01120.x>. The package provides functions for
calculating confidence intervals for the model parameters and for
performing likelihood ratio tests.

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
%{rlibdir}/%{packname}/libs

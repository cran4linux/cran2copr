%global packname  biglasso
%global packver   1.3-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6
Release:          1%{?dist}
Summary:          Extending Lasso Model Fitting to Big Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-bigmemory >= 4.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-bigmemory >= 4.5.0
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-Matrix 
Requires:         R-CRAN-ncvreg 
Requires:         R-methods 

%description
Extend lasso and elastic-net model fitting for ultrahigh-dimensional,
multi-gigabyte data sets that cannot be loaded into memory. It's much more
memory- and computation-efficient as compared to existing lasso-fitting
packages like 'glmnet' and 'ncvreg', thus allowing for very powerful big
data analysis even with an ordinary laptop.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

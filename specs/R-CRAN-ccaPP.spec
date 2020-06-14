%global packname  ccaPP
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          2%{?dist}
Summary:          (Robust) Canonical Correlation Analysis via Projection Pursuit

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-pcaPP >= 1.8.1
BuildRequires:    R-CRAN-RcppArmadillo >= 0.4.100.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-robustbase 
Requires:         R-CRAN-pcaPP >= 1.8.1
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-parallel 
Requires:         R-CRAN-robustbase 

%description
Canonical correlation analysis and maximum correlation via projection
pursuit, as well as fast implementations of correlation estimators, with a
focus on robust and nonparametric methods.

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

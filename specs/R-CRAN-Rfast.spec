%global packname  Rfast
%global packver   1.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.5
Release:          1%{?dist}
Summary:          A Collection of Efficient and Extremely Fast R Functions

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-RcppZiggurat 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-RcppZiggurat 

%description
A collection of fast (utility) functions for data analysis. Column- and
row- wise means, medians, variances, minimums, maximums, many t, F and
G-square tests, many regressions (normal, logistic, Poisson), are some of
the many fast functions. Reference: Tsagris M, Papadakis M. (2018). Taking
R to its limits: 70+ tips. PeerJ Preprints 6:e26605v1
<doi:10.7287/peerj.preprints.26605v1>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

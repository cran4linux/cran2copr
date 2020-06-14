%global packname  steadyICA
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          ICA and Tests of Independence via Multivariate DistanceCovariance

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.9.13
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-combinat 
Requires:         R-CRAN-Rcpp >= 0.9.13
Requires:         R-MASS 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-combinat 

%description
Functions related to multivariate measures of independence and ICA:
-estimate independent components by minimizing distance covariance;
-conduct a test of mutual independence based on distance covariance;
-estimate independent components via infomax (a popular method but
generally performs poorer than mdcovica, ProDenICA, and/or fastICA, but is
useful for comparisons); -order indepedent components by skewness; -match
independent components from multiple estimates; -other functions useful in
ICA.

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

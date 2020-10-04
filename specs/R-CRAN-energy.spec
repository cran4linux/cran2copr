%global packname  energy
%global packver   1.7-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.7
Release:          3%{?dist}%{?buildtag}
Summary:          E-Statistics: Multivariate Inference via the Energy of Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-stats 
BuildRequires:    R-boot 
Requires:         R-CRAN-Rcpp >= 0.12.6
Requires:         R-stats 
Requires:         R-boot 

%description
E-statistics (energy) tests and statistics for multivariate and univariate
inference, including distance correlation, one-sample, two-sample, and
multi-sample tests for comparing multivariate distributions, are
implemented. Measuring and testing multivariate independence based on
distance correlation, partial distance correlation, multivariate
goodness-of-fit tests, k-groups and hierarchical clustering based on
energy distance, testing for multivariate normality, distance components
(disco) for non-parametric analysis of structured data, and other energy
statistics/methods are implemented.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

%global packname  attrCUSUM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Tools for Attribute VSI CUSUM Control Chart

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildRequires:    R-stats >= 3.3.2
BuildRequires:    R-utils >= 3.3.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.500.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
Requires:         R-stats >= 3.3.2
Requires:         R-utils >= 3.3.2
Requires:         R-CRAN-Rcpp >= 0.12.8

%description
An implementation of tools for design of attribute variable sampling
interval cumulative sum chart. It currently provides information for
monitoring of mean increase such as average number of sample to signal,
average time to signal, a matrix of transient probabilities, suitable
control limits when the data are (zero inflated) Poisson/binomial
distribution. Functions in the tools can be easily applied to other count
processes. Also, tools might be extended to more complicated cumulative
sum control chart. We leave these issues as our perpetual work.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

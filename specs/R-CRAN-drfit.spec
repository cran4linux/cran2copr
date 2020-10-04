%global packname  drfit
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          3%{?dist}%{?buildtag}
Summary:          Dose-Response Data Evaluation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-drc 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-qcc 
BuildRequires:    R-CRAN-odbc 
BuildRequires:    R-CRAN-DBI 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-MASS 
Requires:         R-CRAN-drc 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-qcc 
Requires:         R-CRAN-odbc 
Requires:         R-CRAN-DBI 

%description
A somewhat outdated package of basic and easy-to-use functions for fitting
dose-response curves to continuous dose-response data, calculating some
toxicological parameters and plotting the results. Please consider using
the more powerful and actively developed 'drc' package.  Functions that
are fitted are the cumulative density function of the log-normal
distribution ('probit' fit), of the logistic distribution ('logit' fit),
of the Weibull distribution ('weibull' fit) and a linear-logistic model
('linlogit' fit), derived from the latter, which is used to describe data
showing stimulation at low doses (hormesis). In addition, functions
checking, plotting and retrieving dose-response data retrieved from a
database accessed via 'odbc' are included. As an alternative to the
original fitting methods, the algorithms from the 'drc' package can be
used.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

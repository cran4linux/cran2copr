%global __brp_check_rpaths %{nil}
%global packname  carSurv
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Correlation-Adjusted Regression Survival (CARS) Scores

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-CRAN-fdrtool 
Requires:         R-CRAN-Rcpp 
Requires:         R-survival 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-mboost 
Requires:         R-CRAN-fdrtool 

%description
Contains functions to estimate the Correlation-Adjusted Regression
Survival (CARS) Scores. The method is described in Welchowski, T. and
Zuber, V. and Schmid, M., (2018), Correlation-Adjusted Regression Survival
Scores for High-Dimensional Variable Selection, <arXiv:1802.08178>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

%global packname  bnnSurvival
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}
Summary:          Bagged k-Nearest Neighbors Survival Prediction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-pec 
Requires:         R-parallel 
Requires:         R-methods 

%description
Implements a bootstrap aggregated (bagged) version of the k-nearest
neighbors survival probability prediction method (Lowsky et al. 2013). In
addition to the bootstrapping of training samples, the features can be
subsampled in each baselearner to break the correlation between them. The
Rcpp package is used to speed up the computation.

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

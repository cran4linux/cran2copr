%global packname  NCutYX
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Clustering of Omics Data of Multiple Types with a MultilayerNetwork Representation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-fields >= 9.0
BuildRequires:    R-MASS >= 7.3.47
BuildRequires:    R-CRAN-glmnet >= 2.0.5
BuildRequires:    R-CRAN-mvtnorm >= 1.0.6
BuildRequires:    R-CRAN-Rcpp >= 0.12.2
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-fields >= 9.0
Requires:         R-MASS >= 7.3.47
Requires:         R-CRAN-glmnet >= 2.0.5
Requires:         R-CRAN-mvtnorm >= 1.0.6
Requires:         R-CRAN-Rcpp >= 0.12.2

%description
Omics data come in different forms: gene expression, methylation, copy
number, protein measurements and more. 'NCutYX' allows clustering of
variables, of samples, and both variables and samples (biclustering),
while incorporating the dependencies across multiple types of Omics data.
(SJ Teran Hidalgo et al (2017), <doi:10.1186/s12864-017-3990-1>).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

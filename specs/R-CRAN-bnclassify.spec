%global packname  bnclassify
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}
Summary:          Learning Discrete Bayesian Network Classifiers from Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-rpart >= 4.1.8
BuildRequires:    R-CRAN-entropy >= 1.2.0
BuildRequires:    R-CRAN-matrixStats >= 0.14.0
BuildRequires:    R-CRAN-assertthat >= 0.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
Requires:         R-rpart >= 4.1.8
Requires:         R-CRAN-entropy >= 1.2.0
Requires:         R-CRAN-matrixStats >= 0.14.0
Requires:         R-CRAN-assertthat >= 0.1
Requires:         R-CRAN-Rcpp 

%description
State-of-the art algorithms for learning discrete Bayesian network
classifiers from data, including a number of those described in Bielza &
Larranaga (2014) <doi:10.1145/2576868>, with functions for prediction,
model evaluation and inspection.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

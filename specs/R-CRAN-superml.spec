%global __brp_check_rpaths %{nil}
%global packname  superml
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          3%{?dist}%{?buildtag}
Summary:          Build Machine Learning Models Like Using Python's Scikit-LearnLibrary in R

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-R6 >= 2.2
BuildRequires:    R-CRAN-data.table >= 1.10
BuildRequires:    R-CRAN-Rcpp >= 1.0
BuildRequires:    R-CRAN-assertthat >= 0.2
BuildRequires:    R-CRAN-Metrics >= 0.1
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-R6 >= 2.2
Requires:         R-CRAN-data.table >= 1.10
Requires:         R-CRAN-Rcpp >= 1.0
Requires:         R-CRAN-assertthat >= 0.2
Requires:         R-CRAN-Metrics >= 0.1

%description
The idea is to provide a standard interface to users who use both R and
Python for building machine learning models. This package provides a
scikit-learn's fit, predict interface to train machine learning models in
R.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/stopwords
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

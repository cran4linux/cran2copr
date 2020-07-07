%global packname  FSelectorRcpp
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          3%{?dist}
Summary:          'Rcpp' Implementation of 'FSelector' Entropy-Based FeatureSelection Algorithms with a Sparse Matrix Support

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 

%description
'Rcpp' (free of 'Java'/'Weka') implementation of 'FSelector' entropy-based
feature selection algorithms based on an MDL discretization (Fayyad U. M.,
Irani K. B.: Multi-Interval Discretization of Continuous-Valued Attributes
for Classification Learning. In 13'th International Joint Conference on
Uncertainly in Artificial Intelligence (IJCAI93), pages 1022-1029,
Chambery, France, 1993.)
<https://www.ijcai.org/Proceedings/93-2/Papers/022.pdf> with a sparse
matrix support.

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
%doc %{rlibdir}/%{packname}/benchmarks
%doc %{rlibdir}/%{packname}/dev
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

%global __brp_check_rpaths %{nil}
%global packname  discretecdAlgorithm
%global packver   0.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          3%{?dist}%{?buildtag}
Summary:          Coordinate-Descent Algorithm for Learning Sparse DiscreteBayesian Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-sparsebnUtils >= 0.0.4
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-sparsebnUtils >= 0.0.4
Requires:         R-CRAN-igraph 

%description
Structure learning of Bayesian network using coordinate-descent algorithm.
This algorithm is designed for discrete network assuming a multinomial
data set, and we use a multi-logit model to do the regression. The
algorithm is described in Gu, Fu and Zhou (2016) <arXiv:1403.2310>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

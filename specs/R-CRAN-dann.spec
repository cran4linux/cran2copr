%global packname  dann
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Discriminant Adaptive Nearest Neighbor Classification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-MASS >= 7.3
BuildRequires:    R-stats >= 3.5.3
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-fpc >= 2.1.11.1
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-MASS >= 7.3
Requires:         R-stats >= 3.5.3
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-fpc >= 2.1.11.1
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-purrr >= 0.3.2

%description
Discriminant Adaptive Nearest Neighbor Classification is a variation of k
nearest neighbors where the neighborhood is elongated along class
boundaries. This package implements dann and sub_dann from Hastie (1995)
<https://web.stanford.edu/~hastie/Papers/dann_IEEE.pdf>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

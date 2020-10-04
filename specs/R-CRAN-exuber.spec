%global packname  exuber
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Econometric Analysis of Explosive Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-doRNG >= 1.8.2
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-glue >= 1.3.1
BuildRequires:    R-CRAN-cli >= 1.1.0
BuildRequires:    R-CRAN-doSNOW >= 1.0.16
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.400.2.0
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-vctrs >= 0.2.4
BuildRequires:    R-CRAN-generics >= 0.0.2
BuildRequires:    R-parallel 
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-doRNG >= 1.8.2
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-glue >= 1.3.1
Requires:         R-CRAN-cli >= 1.1.0
Requires:         R-CRAN-doSNOW >= 1.0.16
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-vctrs >= 0.2.4
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-generics >= 0.0.2
Requires:         R-parallel 

%description
Testing for and dating periods of explosive dynamics (exuberance) in time
series using the univariate and panel recursive unit root tests proposed
by Phillips et al. (2015) <doi:10.1111/iere.12132> and Pavlidis et al.
(2016) <doi:10.1007/s11146-015-9531-2>.  The recursive least-squares
algorithm utilizes the matrix inversion lemma to avoid matrix inversion
which results in significant speed improvements. Simulation of a variety
of periodically-collapsing bubble processes.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

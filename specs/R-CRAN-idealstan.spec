%global packname  idealstan
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}
Summary:          Generalized IRT Ideal Point Models with 'Stan'

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-rstan >= 2.18.2
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66
BuildRequires:    R-CRAN-rstantools >= 1.5.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-svDialogs 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shinystan 
BuildRequires:    R-CRAN-gghighlight 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-rstan >= 2.18.2
Requires:         R-CRAN-rstantools >= 1.5.1
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-svDialogs 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shinystan 
Requires:         R-CRAN-gghighlight 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggrepel 

%description
Offers item-response theory (IRT) ideal-point estimation for binary,
ordinal, counts and continuous responses with time-varying and
missing-data inference. Full and approximate Bayesian sampling with 'Stan'
(<https://mc-stan.org/>).

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

%global packname  skpr
%global packver   0.64.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.64.2
Release:          2%{?dist}
Summary:          Design of Experiments Suite: Generate and Evaluate OptimalDesigns

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-stats 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-rintrojs 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-shiny 
Requires:         R-utils 
Requires:         R-CRAN-iterators 
Requires:         R-stats 
Requires:         R-nlme 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-rintrojs 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-survival 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-future 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-car 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lmerTest 
Requires:         R-methods 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-crayon 

%description
Generates and evaluates D, I, A, Alias, E, T, and G optimal designs.
Supports generation and evaluation of blocked and
split/split-split/.../N-split plot designs. Includes parametric and Monte
Carlo power evaluation functions, and supports calculating power for
censored responses. Provides a framework to evaluate power using functions
provided in other packages or written by the user. Includes a Shiny
graphical user interface that displays the underlying code used to create
and evaluate the design to improve ease-of-use and make analyses more
reproducible.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

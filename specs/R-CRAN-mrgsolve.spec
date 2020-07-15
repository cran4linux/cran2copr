%global packname  mrgsolve
%global packver   0.10.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.4
Release:          3%{?dist}
Summary:          Simulate from ODE-Based Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-BH >= 1.62.0.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.900.2.0
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-tidyselect >= 0.2.5
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-RcppArmadillo >= 0.7.900.2.0
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-tidyselect >= 0.2.5
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-methods 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-glue 

%description
Fast simulation from ordinary differential equation (ODE) based models
typically employed in quantitative pharmacology and systems biology.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/base
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/models
%doc %{rlibdir}/%{packname}/mrgx
%doc %{rlibdir}/%{packname}/msg
%doc %{rlibdir}/%{packname}/nonmem
%doc %{rlibdir}/%{packname}/project
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/Rmd
%doc %{rlibdir}/%{packname}/script
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

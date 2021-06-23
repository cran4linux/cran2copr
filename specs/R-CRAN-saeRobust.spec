%global __brp_check_rpaths %{nil}
%global packname  saeRobust
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Robust Small Area Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-aoos 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-modules 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-aoos 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-ggplot2 
Requires:         R-Matrix 
Requires:         R-CRAN-magrittr 
Requires:         R-MASS 
Requires:         R-CRAN-modules 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-spdep 

%description
Methods to fit robust alternatives to commonly used models used in Small
Area Estimation. The methods here used are based on best linear unbiased
predictions and linear mixed models. At this time available models include
area level models incorporating spatial and temporal correlation in the
random effects.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/Readme.Rmd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

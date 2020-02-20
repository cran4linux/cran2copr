%global packname  mets
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          1%{?dist}
Summary:          Analysis of Multivariate Event Times

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-survival >= 2.43.1
BuildRequires:    R-CRAN-timereg >= 1.9.4
BuildRequires:    R-CRAN-lava >= 1.6.6
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-survival >= 2.43.1
Requires:         R-CRAN-timereg >= 1.9.4
Requires:         R-CRAN-lava >= 1.6.6
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Rcpp 
Requires:         R-splines 

%description
Implementation of various statistical models for multivariate event
history data <doi:10.1007/s10985-013-9244-x>. Including multivariate
cumulative incidence models <doi:10.1002/sim.6016>, and bivariate random
effects probit models (Liability models) <doi:10.1016/j.csda.2015.01.014>.
Also contains two-stage binomial modelling that can do pairwise odds-ratio
dependence modelling based marginal logistic regression models. This is an
alternative to the alternating logistic regression approach (ALR).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/devel
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/documentation
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

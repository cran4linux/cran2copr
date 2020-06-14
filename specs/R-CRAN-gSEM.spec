%global packname  gSEM
%global packver   0.4.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3.4
Release:          2%{?dist}
Summary:          Semi-Supervised Generalized Structural Equation Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-DiagrammeR 
Requires:         R-CRAN-knitr 
Requires:         R-MASS 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-DiagrammeR 

%description
Conducts a semi-gSEM statistical analysis (semi-supervised generalized
structural equation modeling) on a data frame of coincident observations
of multiple predictive or intermediate variables and a final continuous,
outcome variable, via two functions sgSEMp1() and sgSEMp2(), representing
fittings based on two statistical principles. Principle 1 determines all
sensible univariate relationships in the spirit of the Markovian process.
The relationship between each pair of variables, including predictors and
the final outcome variable, is determined with the Markovian property that
the value of the current predictor is sufficient in relating to the next
level variable, i.e., the relationship is independent of the specific
value of the preceding-level variables to the current predictor, given the
current value. Principle 2 resembles the multiple regression principle in
the way multiple predictors are considered simultaneously. Specifically,
the relationship of the first-level predictors (such as Time and
irradiance etc) to the outcome variable (such as, module degradation or
yellowing) is fit by a supervised additive model. Then each significant
intermediate variable is taken as the new outcome variable and the other
variables (except the final outcome variable) as the predictors in
investigating the next-level multivariate relationship by a supervised
additive model. This fitting process is continued until all sensible
models are investigated.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

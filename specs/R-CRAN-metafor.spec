%global packname  metafor
%global packver   2.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0
Release:          2%{?dist}
Summary:          Meta-Analysis Package for R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-nlme 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-nlme 

%description
A comprehensive collection of functions for conducting meta-analyses in R.
The package includes functions to calculate various effect sizes or
outcome measures, fit fixed-, random-, and mixed-effects models to such
data, carry out moderator and meta-regression analyses, and create various
types of meta-analytical plots (e.g., forest, funnel, radial, L'Abbe,
Baujat, GOSH plots). For meta-analyses of binomial and person-time data,
the package also provides functions that implement specialized methods,
including the Mantel-Haenszel method, Peto's method, and a variety of
suitable generalized linear (mixed-effects) models (i.e., mixed-effects
logistic and Poisson regression models). Finally, the package provides
functionality for fitting meta-analytic multivariate/multilevel models
that account for non-independent sampling errors and/or true effects
(e.g., due to the inclusion of multiple treatment studies, multiple
endpoints, or other forms of clustering). Network meta-analyses and
meta-analyses accounting for known correlation structures (e.g., due to
phylogenetic relatedness) can also be conducted.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/reporter
%{rlibdir}/%{packname}/INDEX

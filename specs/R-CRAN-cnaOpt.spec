%global __brp_check_rpaths %{nil}
%global packname  cnaOpt
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimizing Consistency and Coverage in Configurational Causal Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-cna >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cna >= 3.0.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-utils 

%description
This is an add-on to the 'cna' package
<https://CRAN.R-project.org/package=cna> comprising various functions for
optimizing consistency and coverage scores of models of configurational
comparative methods as Coincidence Analysis (CNA) and Qualitative
Comparative Analysis (QCA). The function conCovOpt() calculates con-cov
optima, selectMax() selects con-cov maxima among the con-cov optima,
DNFbuild() can be used to build models actually reaching those optima, and
findOutcomes() identifies those factor values in analyzed data that can be
modeled as outcomes. For a theoretical introduction to these functions see
<https://people.uib.no/mba110/docs/ConCovOpt.pdf>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

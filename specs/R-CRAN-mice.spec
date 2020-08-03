%global packname  mice
%global packver   3.10.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.10.0.1
Release:          1%{?dist}
Summary:          Multivariate Imputation by Chained Equations

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-graphics 
BuildRequires:    R-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-generics 
Requires:         R-graphics 
Requires:         R-lattice 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
Multiple imputation using Fully Conditional Specification (FCS)
implemented by the MICE algorithm as described in Van Buuren and
Groothuis-Oudshoorn (2011) <doi:10.18637/jss.v045.i03>. Each variable has
its own imputation model. Built-in imputation models are provided for
continuous data (predictive mean matching, normal), binary data (logistic
regression), unordered categorical data (polytomous logistic regression)
and ordered categorical data (proportional odds). MICE can also impute
continuous two-level data (normal model, pan, second-level variables).
Passive imputation can be used to maintain consistency between variables.
Various diagnostic plots are available to inspect the quality of the
imputations.

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

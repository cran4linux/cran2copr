%global packname  glmulti
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          3%{?dist}%{?buildtag}
Summary:          Model Selection and Multimodel Inference Made Easy

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 0.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-leaps 
Requires:         R-CRAN-rJava >= 0.5.0
Requires:         R-methods 
Requires:         R-CRAN-leaps 

%description
Automated model selection and model-averaging. Provides a wrapper for glm
and other functions, automatically generating all possible models (under
constraints set by the user) with the specified response and explanatory
variables, and finding the best models in terms of some Information
Criterion (AIC, AICc or BIC). Can handle very large numbers of candidate
models. Features a Genetic Algorithm to find the best models when an
exhaustive screening of the candidates is not feasible.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX

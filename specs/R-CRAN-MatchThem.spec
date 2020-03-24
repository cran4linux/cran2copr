%global packname  MatchThem
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          1%{?dist}
Summary:          Matching and Weighting Multiply Imputed Datasets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-WeightIt 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-WeightIt 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-mice 
Requires:         R-stats 
Requires:         R-CRAN-survey 

%description
Provides the necessary tools for the pre-processing techniques of matching
and weighting multiply imputed datasets to control for effects of
confounders and to reduce the degree of dependence on certain modeling
assumptions in studying the causal associations between an exposure and an
outcome. This package includes functions to perform matching within and
across the multiply imputed datasets using several matching methods, to
estimate weights of units in the imputed datasets using several weighting
methods, to calculate the causal effect estimate in each matched or
weighted dataset using parametric or non-parametric statistical models,
and to pool the obtained estimates from these models according to Rubin's
rules (please see <https://github.com/FarhadPishgar/MatchThem> for
details).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

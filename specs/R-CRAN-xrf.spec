%global __brp_check_rpaths %{nil}
%global packname  xrf
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          eXtreme RuleFit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 3.0
BuildRequires:    R-CRAN-xgboost >= 0.71.2
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fuzzyjoin 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
Requires:         R-CRAN-glmnet >= 3.0
Requires:         R-CRAN-xgboost >= 0.71.2
Requires:         R-Matrix 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fuzzyjoin 
Requires:         R-CRAN-rlang 
Requires:         R-methods 

%description
An implementation of the RuleFit algorithm as described in Friedman &
Popescu (2008) <doi:10.1214/07-AOAS148>. eXtreme Gradient Boosting
('XGBoost') is used to build rules, and 'glmnet' is used to fit a sparse
linear model on the raw and rule features. The result is a model that
learns similarly to a tree ensemble, while often offering improved
interpretability and achieving improved scoring runtime in live
applications. Several algorithms for reducing rule complexity are
provided, most notably hyperrectangle de-overlapping. All algorithms scale
to several million rows and support sparse representations to handle tens
of thousands of dimensions.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

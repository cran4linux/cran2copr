%global packname  mlr
%global packver   2.17.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.17.1
Release:          2%{?dist}
Summary:          Machine Learning in R

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-checkmate >= 1.8.2
BuildRequires:    R-CRAN-parallelMap >= 1.3
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-CRAN-BBmisc >= 1.11
BuildRequires:    R-CRAN-ParamHelpers >= 1.10
BuildRequires:    R-CRAN-backports >= 1.1.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-survival 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-checkmate >= 1.8.2
Requires:         R-CRAN-parallelMap >= 1.3
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-CRAN-BBmisc >= 1.11
Requires:         R-CRAN-ParamHelpers >= 1.10
Requires:         R-CRAN-backports >= 1.1.0
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-survival 
Requires:         R-utils 
Requires:         R-CRAN-XML 

%description
Interface to a large number of classification and regression techniques,
including machine-readable parameter descriptions. There is also an
experimental extension for survival analysis, clustering and general,
example-specific cost-sensitive learning. Generic resampling, including
cross-validation, bootstrapping and subsampling. Hyperparameter tuning
with modern optimization techniques, for single- and multi-objective
problems. Filter and wrapper methods for feature selection. Extension of
basic learners with additional operations common in machine learning, also
allowing for easy nested resampling. Most operations can be parallelized.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/makeData.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

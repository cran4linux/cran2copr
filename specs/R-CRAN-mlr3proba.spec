%global packname  mlr3proba
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Probabilistic Supervised Learning for 'mlr3'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-distr6 >= 1.3.6
BuildRequires:    R-CRAN-mlr3 >= 0.1.8
BuildRequires:    R-CRAN-mlr3misc >= 0.1.7
BuildRequires:    R-CRAN-paradox >= 0.1.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-mlr3pipelines 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-survival 
Requires:         R-CRAN-distr6 >= 1.3.6
Requires:         R-CRAN-mlr3 >= 0.1.8
Requires:         R-CRAN-mlr3misc >= 0.1.7
Requires:         R-CRAN-paradox >= 0.1.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-mlr3pipelines 
Requires:         R-CRAN-R6 
Requires:         R-survival 

%description
Provides extensions for probabilistic supervised learning for 'mlr3'.
This includes extending the regression task to probabilistic and interval
regression, adding a survival task, and other specialized models,
predictions, and measures.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/references.bib
%doc %{rlibdir}/%{packname}/testthat
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

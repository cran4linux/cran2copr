%global packname  OptimClassifier
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}
Summary:          Create the Best Train for Classification Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-rpart 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-clisymbols 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-MASS 
Requires:         R-CRAN-lme4 
Requires:         R-rpart 
Requires:         R-nnet 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-clisymbols 
Requires:         R-CRAN-ggplot2 

%description
Patterns searching and binary classification in economic and financial
data is a large field of research. There are a large part of the data that
the target variable is binary. Nowadays, many methodologies are used, this
package collects most popular and compare different configuration options
for Linear Models (LM), Generalized Linear Models (GLM), Linear Mixed
Models (LMM), Discriminant Analysis (DA), Classification And Regression
Trees (CART), Neural Networks (NN) and Support Vector Machines (SVM).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

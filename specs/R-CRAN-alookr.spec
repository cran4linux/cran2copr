%global packname  alookr
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}
Summary:          Model Classifier for Binary Classification

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-dlookr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-ggmosaic 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-unbalanced 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-MLmetrics 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-dlookr 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-ggmosaic 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-unbalanced 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-party 
Requires:         R-rpart 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-MLmetrics 
Requires:         R-MASS 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-future 
Requires:         R-CRAN-purrr 

%description
A collection of tools that support data splitting, predictive modeling,
and model evaluation. A typical function is to split a dataset into a
training dataset and a test dataset. Then compare the data distribution of
the two datasets. Another feature is to support the development of
predictive models and to compare the performance of several predictive
models, helping to select the best model.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

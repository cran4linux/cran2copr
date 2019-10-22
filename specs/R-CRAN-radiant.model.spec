%global packname  radiant.model
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Model Menu for Radiant: Business Analytics using R and Shiny

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-nnet >= 7.3.12
BuildRequires:    R-rpart >= 4.1.11
BuildRequires:    R-CRAN-sandwich >= 2.3.4
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-car >= 2.1.3
BuildRequires:    R-CRAN-gridExtra >= 2.0
BuildRequires:    R-CRAN-psych >= 1.8.4
BuildRequires:    R-CRAN-lubridate >= 1.7.2
BuildRequires:    R-CRAN-e1071 >= 1.6.8
BuildRequires:    R-CRAN-NeuralNetTools >= 1.5.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-CRAN-stringr >= 1.1.0
BuildRequires:    R-CRAN-import >= 1.1.0
BuildRequires:    R-CRAN-radiant.data >= 1.0.0
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.0
BuildRequires:    R-CRAN-radiant.basics >= 0.9.9
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-data.tree >= 0.7.4
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-yaml 
Requires:         R-nnet >= 7.3.12
Requires:         R-rpart >= 4.1.11
Requires:         R-CRAN-sandwich >= 2.3.4
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-car >= 2.1.3
Requires:         R-CRAN-gridExtra >= 2.0
Requires:         R-CRAN-psych >= 1.8.4
Requires:         R-CRAN-lubridate >= 1.7.2
Requires:         R-CRAN-e1071 >= 1.6.8
Requires:         R-CRAN-NeuralNetTools >= 1.5.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-CRAN-stringr >= 1.1.0
Requires:         R-CRAN-import >= 1.1.0
Requires:         R-CRAN-radiant.data >= 1.0.0
Requires:         R-CRAN-DiagrammeR >= 1.0.0
Requires:         R-CRAN-radiant.basics >= 0.9.9
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-data.tree >= 0.7.4
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-yaml 

%description
The Radiant Model menu includes interfaces for linear and logistic
regression, naive Bayes, neural networks, classification and regression
trees, model evaluation, collaborative filtering, decision analysis, and
simulation. The application extends the functionality in radiant.data.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/app
%{rlibdir}/%{packname}/INDEX

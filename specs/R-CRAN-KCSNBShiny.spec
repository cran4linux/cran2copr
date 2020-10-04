%global packname  KCSNBShiny
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Naive Bayes Classifier

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-e1071 

%description
Predicts any variable in any categorical dataset for given values of
predictor variables. If a dataset contains 4 variables, then any variable
can be predicted based on the values of the other three variables given by
the user. The user can upload their own datasets and select what variable
they want to predict. A 'handsontable' is provided to enter the predictor
values and also accuracy of the prediction is also shown.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

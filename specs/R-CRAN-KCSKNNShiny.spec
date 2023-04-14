%global __brp_check_rpaths %{nil}
%global packname  KCSKNNShiny
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          K-Nearest Neighbour Classifier

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
BuildRequires:    R-CRAN-FNN 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-FNN 

%description
It predicts any attribute (categorical) given a set of input numeric
predictor values. Note that only numeric input predictors should be given.
The k value can be chosen according to accuracies provided. The attribute
to be predicted can be selected from the dropdown provided (select
categorical attribute). This is because categorical attributes cannot be
given as inputs here. A 'handsontable' is also provided to enter the input
predictor values.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

%global packname  shinyr
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}
Summary:          Data Insights Through Inbuilt R Shiny App

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-DMwR 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-DMwR 
Requires:         R-CRAN-caret 
Requires:         R-nnet 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-knitr 

%description
It builds dynamic R shiny based dashboards to analyze any CSV files. It
provides simple dashboard design to subset the data, perform exploratory
data analysis and preliminary machine learning (supervised and
unsupervised). It also provides filters based on columns of interest.

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
%doc %{rlibdir}/%{packname}/app
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

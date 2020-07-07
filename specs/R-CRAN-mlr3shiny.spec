%global packname  mlr3shiny
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Machine Learning in 'shiny' with 'mlr3'

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-DT >= 0.11
BuildRequires:    R-CRAN-mlr3 >= 0.1.6
BuildRequires:    R-CRAN-mlr3measures >= 0.1.1
BuildRequires:    R-CRAN-mlr3learners 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-DT >= 0.11
Requires:         R-CRAN-mlr3 >= 0.1.6
Requires:         R-CRAN-mlr3measures >= 0.1.1
Requires:         R-CRAN-mlr3learners 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-e1071 
Requires:         R-stats 

%description
A web-based graphical user interface to provide the basic steps of a
machine learning workflow. It uses the functionalities of the 'mlr3'
framework.

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
%doc %{rlibdir}/%{packname}/mlr3shiny
%{rlibdir}/%{packname}/INDEX

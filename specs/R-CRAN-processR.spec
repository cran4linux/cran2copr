%global packname  processR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Implementation of the 'PROCESS' Macro

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.6.3
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggiraphExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jtools 
BuildRequires:    R-CRAN-mycor 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rrtable 
BuildRequires:    R-CRAN-semTools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-modelr 
BuildRequires:    R-CRAN-prediction 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-TH.data 
BuildRequires:    R-CRAN-shinyWidgets 
Requires:         R-CRAN-lavaan >= 0.6.3
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggiraphExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jtools 
Requires:         R-CRAN-mycor 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rrtable 
Requires:         R-CRAN-semTools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-modelr 
Requires:         R-CRAN-prediction 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-TH.data 
Requires:         R-CRAN-shinyWidgets 

%description
Perform moderation, mediation, moderated mediation and moderated
moderation. Inspired from famous 'PROCESS' macro for 'SPSS' and 'SAS'
created by Andrew Hayes.

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
%doc %{rlibdir}/%{packname}/figures
%doc %{rlibdir}/%{packname}/showModels
%{rlibdir}/%{packname}/INDEX

%global packname  teachingApps
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          3%{?dist}%{?buildtag}
Summary:          Apps for Teaching Statistics, R Programming, and Shiny AppDevelopment

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-BH >= 1.58.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-pacman 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcppNumerical 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-pacman 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-datasets 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-markdown 
Requires:         R-stats 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rprojroot 
Requires:         R-utils 
Requires:         R-CRAN-devtools 
Requires:         R-graphics 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RcppNumerical 
Requires:         R-CRAN-miniUI 

%description
Contains apps and gadgets for teaching data analysis and statistics
concepts along with how to implement them in R.  Includes tools to make
app development easier and faster by nesting apps together.

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
%doc %{rlibdir}/%{packname}/apps
%doc %{rlibdir}/%{packname}/figure
%doc %{rlibdir}/%{packname}/gadget_test.html
%doc %{rlibdir}/%{packname}/gadget_test.Rmd
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/teachingApps
%doc %{rlibdir}/%{packname}/test.html
%doc %{rlibdir}/%{packname}/test.Rhtml
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

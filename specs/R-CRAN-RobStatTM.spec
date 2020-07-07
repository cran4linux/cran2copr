%global packname  RobStatTM
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Robust Statistics: Theory and Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-fit.models 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DEoptimR 
BuildRequires:    R-CRAN-pyinit 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-xts 
Requires:         R-CRAN-fit.models 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-DEoptimR 
Requires:         R-CRAN-pyinit 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-xts 

%description
Companion package for the book: "Robust Statistics: Theory and Methods,
second edition", <http://www.wiley.com/go/maronna/robust>.  This package
contains code that implements the robust estimators discussed in the
recent second edition of the book above, as well as the scripts
reproducing all the examples in the book.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/shiny-ui
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

%global packname  sdcMicro
%global packver   5.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.5.0
Release:          1%{?dist}
Summary:          Statistical Disclosure Control Methods for Anonymization of Dataand Risk Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-VIM >= 4.7.0
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-carData 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-cluster 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-prettydoc 
Requires:         R-CRAN-VIM >= 4.7.0
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-car 
Requires:         R-CRAN-carData 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-robustbase 
Requires:         R-cluster 
Requires:         R-MASS 
Requires:         R-CRAN-e1071 
Requires:         R-tools 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-prettydoc 

%description
Data from statistical agencies and other institutions are mostly
confidential. This package (see also Templ, Kowarik and Meindl (2017)
<doi:10.18637/jss.v067.i04>) can be used for the generation of anonymized
(micro)data, i.e. for the creation of public- and scientific-use files.
The theoretical basis for the methods implemented can be found in Templ
(2017) <doi:10.1007/978-3-319-50272-4>. Various risk estimation and
anonymisation methods are included. Note that the package includes a
graphical user interface (Meindl and Templ, 2019 <doi:10.3390/a12090191>)
that allows to use various methods of this package.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

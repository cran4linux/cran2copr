%global packname  VIM
%global packver   5.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.0
Release:          1%{?dist}
Summary:          Visualization and Imputation of Missing Values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-data.table >= 1.9.4
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-MASS 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-laeken 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-data.table >= 1.9.4
Requires:         R-CRAN-colorspace 
Requires:         R-grid 
Requires:         R-CRAN-car 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-vcd 
Requires:         R-MASS 
Requires:         R-nnet 
Requires:         R-CRAN-e1071 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-laeken 
Requires:         R-CRAN-ranger 

%description
New tools for the visualization of missing and/or imputed values are
introduced, which can be used for exploring the data and the structure of
the missing and/or imputed values. Depending on this structure of the
missing values, the corresponding methods may help to identify the
mechanism generating the missing values and allows to explore the data
including missing values. In addition, the quality of imputation can be
visually explored using various univariate, bivariate, multiple and
multivariate plot methods (<doi:10.1007/s11634-011-0102-y>). A graphical
user interface available in the separate package VIMGUI allows an easy
handling of the implemented plot methods. Fast imputation methods such as
k-nearest neighbor imputation (<doi:10.18637/jss.v074.i07>) and imputation
using robust methods are provided (<doi:10.1016/j.csda.2011.04.012>).

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

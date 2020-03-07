%global packname  Gmisc
%global packver   1.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.2
Release:          1%{?dist}
Summary:          Descriptive Statistics, Transition Plots, and More

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-htmlTable >= 1.13
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-htmlTable >= 1.13
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-lattice 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-forestplot 
Requires:         R-CRAN-abind 
Requires:         R-methods 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-XML 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-stringr 

%description
Tools for making the descriptive "Table 1" used in medical articles, a
transition plot for showing changes between categories (also known as a
Sankey diagram), flow charts by extending the grid package, a method for
variable selection based on the SVD, Bézier lines with arrows
complementing the ones in the 'grid' package, and more.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/rmarkdown
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

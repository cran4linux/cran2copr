%global packname  circumplex
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis and Visualization of Circular Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-glue >= 1.4.0
BuildRequires:    R-boot >= 1.3.18
BuildRequires:    R-CRAN-htmlTable >= 1.13.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.4.6
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-ggforce >= 0.3.0
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-glue >= 1.4.0
Requires:         R-boot >= 1.3.18
Requires:         R-CRAN-htmlTable >= 1.13.3
Requires:         R-CRAN-Rcpp >= 1.0.4.6
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-ggforce >= 0.3.0
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-stats 

%description
Tools for analyzing and visualizing circular data, including scoring
functions for relevant instruments and a generalization of the
bootstrapped structural summary method from Zimmermann & Wright (2017)
<doi:10.1177/1073191115621795> and functions for creating
publication-ready tables and figures from the results. Future versions
will include tools for circular fit and reliability analyses, as well as
visualization enhancements.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

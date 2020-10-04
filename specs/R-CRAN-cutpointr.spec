%global packname  cutpointr
%global packver   1.0.32
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.32
Release:          2%{?dist}%{?buildtag}
Summary:          Determine and Evaluate Optimal Cutpoints in BinaryClassification Tasks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.2
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-gridExtra >= 2.2
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-stats 
Requires:         R-utils 

%description
Estimate cutpoints that optimize a specified metric in binary
classification tasks and validate performance using bootstrapping. Some
methods for more robust cutpoint estimation are supported, e.g. a
parametric method assuming normal distributions, bootstrapped cutpoints,
and smoothing of the metric values per cutpoint using Generalized Additive
Models. Various plotting functions are included. For an overview of the
package see 'Thiele and Hirschfeld (2020)' <arXiv:2002.09209>.

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

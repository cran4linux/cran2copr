%global packname  nanny
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          3%{?dist}
Summary:          High-Level Data Analysis and Manipulation in 'tidyverse' Style

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-widyr 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-methods 
Requires:         R-CRAN-lme4 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-widyr 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-gtools 

%description
Includes wrapper functions for the main high-level data analysis and
manipulations, such as cluster, dimensionality reduction, redundancy
elimination, identify variable elements. It operates on tidy data frames
with element, feature and value column.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/logo-01.png
%doc %{rlibdir}/%{packname}/logo-02.png
%doc %{rlibdir}/%{packname}/logo.ai
%{rlibdir}/%{packname}/INDEX

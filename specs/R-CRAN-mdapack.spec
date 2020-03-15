%global packname  mdapack
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Medical Data Analysis Pack

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-spelling 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-covr 
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-curl 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-spelling 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-covr 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-git2r 
Requires:         R-CRAN-pkgbuild 
Requires:         R-utils 
Requires:         R-CRAN-curl 

%description
An implementation of two functions for medical data analysis which perform
basic univariate analysis and plot heatmaps of numeric variables.Kirkwood
et al. (2003) <doi/abs/10.1002/sim.1961>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

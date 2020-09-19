%global packname  EFAtools
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Flexible Implementations of Exploratory Factor Analysis Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-viridisLite 
Requires:         R-graphics 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-future 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-checkmate 

%description
Provides functions to perform exploratory factor analysis (EFA) procedures
and compare their solutions. The goal is to provide state-of-the-art
factor retention methods and a high degree of flexibility in the EFA
procedures. This way, for example, implementations from R 'psych' and
'SPSS' can be compared. Moreover, functions for Schmid-Leiman
transformation and the computation of omegas are provided. To speed up the
analyses, some of the iterative procedures, like principal axis factoring
(PAF), are implemented in C++.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

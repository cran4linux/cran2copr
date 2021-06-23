%global __brp_check_rpaths %{nil}
%global packname  DAMisc
%global packver   1.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          Dave Armstrong's Miscellaneous Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-effects 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-optiscale 
BuildRequires:    R-CRAN-AICcmodavg 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-clarkeTest 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-jtools 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-lattice 
Requires:         R-grid 
Requires:         R-CRAN-car 
Requires:         R-CRAN-effects 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nnet 
Requires:         R-splines 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-optiscale 
Requires:         R-CRAN-AICcmodavg 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-clarkeTest 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-jtools 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-rstantools

%description
Miscellaneous set of functions I use in my teaching either at the
University of Western Ontario or the Inter-university Consortium for
Political and Social Research (ICPSR) Summer Program in Quantitative
Methods.  Broadly, the functions help with presentation and interpretation
of LMs and GLMs, but also implement some new tools like Alternating Least
Squares Optimal Scaling for dependent variables, a Bayesian analog to the
ALSOS algorithm.  There are also tools to help understand interactions in
both LMs and binary GLMs.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

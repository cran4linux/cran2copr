%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  irtQ
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Unidimensional Item Response Theory Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-mirt 
Requires:         R-stats 
Requires:         R-CRAN-statmod 
Requires:         R-utils 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-parallel 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-mirt 

%description
Fit unidimensional item response theory (IRT) models to a mixture of
dichotomous and polytomous data, calibrate online item parameters (i.e.,
pretest and operational items), estimate examinees' abilities, and examine
the IRT model-data fit on item-level in different ways as well as provide
useful functions related to IRT analyses such as IRT model-data fit
evaluation and differential item functioning analysis. The
bring.flexmirt() and write.flexmirt() functions were written by modifying
the read.flexmirt() function (Pritikin & Falk (2022)
<doi:10.1177/0146621620929431>). The bring.bilog() and bring.parscale()
functions were written by modifying the read.bilog() and read.parscale()
functions, respectively (Weeks (2010) <doi:10.18637/jss.v035.i12>). The
bisection() function was written by modifying the bisection() function
(Howard (2017, ISBN:9780367657918)). The code of the inverse test
characteristic curve scoring in the est_score() function was written by
modifying the irt.eq.tse() function (González (2014)
<doi:10.18637/jss.v059.i07>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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

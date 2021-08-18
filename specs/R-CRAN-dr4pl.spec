%global __brp_check_rpaths %{nil}
%global packname  dr4pl
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dose Response Data Analysis using the 4 Parameter Logistic (4pl) Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-tensor 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-tensor 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-glue 

%description
Models the relationship between dose levels and responses in a
pharmacological experiment using the 4 Parameter Logistic model.
Traditional packages on dose-response modelling such as 'drc' and 'nplr'
often draw errors due to convergence failure especially when data have
outliers or non-logistic shapes. This package provides robust estimation
methods that are less affected by outliers and other initialization
methods that work well for data lacking logistic shapes. We provide the
bounds on the parameters of the 4PL model that prevent parameter estimates
from diverging or converging to zero and base their justification in a
statistical principle. These methods are used as remedies to convergence
failure problems.  Gadagkar, S. R. and Call, G. B. (2015)
<doi:10.1016/j.vascn.2014.08.006> Ritz, C. and Baty, F. and Streibig, J.
C. and Gerhard, D. (2015) <doi:10.1371/journal.pone.0146021>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rprofet
%global packver   3.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          WOE Transformation and Scorecard Builder

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-binr 
BuildRequires:    R-CRAN-ClustOfVar 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ROCit 
Requires:         R-CRAN-binr 
Requires:         R-CRAN-ClustOfVar 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ROCit 

%description
Performs all steps in the credit scoring process. This package allows the
user to follow all the necessary steps for building an effective
scorecard. It provides the user functions for coarse binning of variables,
Weights of Evidence (WOE) transformation, variable clustering, custom
binning, visualization, and scaling of logistic regression coefficients.
The results will generate a scorecard that can be used as an effective
credit scoring tool to evaluate risk. For complete details on the credit
scoring process, see Siddiqi (2005, ISBN:047175451X).

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  frailtyEM
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Frailty Models with the EM Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-expint 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-Rcpp >= 0.12.8
Requires:         R-CRAN-survival 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-expint 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-numDeriv 

%description
Contains functions for fitting shared frailty models with a
semi-parametric baseline hazard with the Expectation-Maximization
algorithm. Supported data formats include clustered failures with left
truncation and recurrent events in gap-time or Andersen-Gill format.
Several frailty distributions, such as the the gamma, positive stable and
the Power Variance Family are supported.

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

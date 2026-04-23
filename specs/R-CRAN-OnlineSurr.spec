%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OnlineSurr
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Surrogate Evaluation for Jointly Longitudinal Outcome and Surrogate

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-kDGLM >= 1.2.14
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-kDGLM >= 1.2.14
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-Rdpack 

%description
Tools for surrogate evaluation in longitudinal studies using state-space
models as proposed in Santos Jr. and Parast
(2026)<doi:10.48550/arXiv.2604.12882>. The package estimates treatment
effects over time with and without adjustment for surrogate information,
summarizes the proportion of treatment effect explained by a longitudinal
surrogate, quantifies uncertainty via bootstrap resampling, and provides
plotting and summary utilities for fitted models.

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

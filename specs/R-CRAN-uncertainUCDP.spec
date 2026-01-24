%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  uncertainUCDP
%global packver   0.7.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.6
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Mixture Models for Uncertainty Estimation of Fatalities in UCDP Conflict Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Provides functions for estimating uncertainty in the number of fatalities
in the Uppsala Conflict Data Program (UCDP) data. The package implements a
parametric reported-value Gumbel mixture distribution that accounts for
the uncertainty in the number of fatalities in the UCDP data. The model is
based on information from a survey on UCDP coders and how they view the
uncertainty of the number of fatalities from UCDP events. The package
provides functions for making random draws of fatalities from the mixture
distribution, as well as to estimate percentiles, quantiles, means, and
other statistics of the distribution. Full details on the survey and
estimation procedure can be found in Vesco et al (2024).

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

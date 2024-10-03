%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gfoRmula
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric G-Formula

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-truncreg 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-grDevices 
Requires:         R-CRAN-nnet 
Requires:         R-parallel 
Requires:         R-CRAN-progress 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-truncreg 
Requires:         R-utils 

%description
Implements the non-iterative conditional expectation (NICE) algorithm of
the g-formula algorithm (Robins (1986) <doi:10.1016/0270-0255(86)90088-6>,
Hernán and Robins (2024, ISBN:9781420076165)). The g-formula can estimate
an outcome's counterfactual mean or risk under hypothetical treatment
strategies (interventions) when there is sufficient information on
time-varying treatments and confounders. This package can be used for
discrete or continuous time-varying treatments and for failure time
outcomes or continuous/binary end of follow-up outcomes. The package can
handle a random measurement/visit process and a priori knowledge of the
data structure, as well as censoring (e.g., by loss to follow-up) and two
options for handling competing events for failure time outcomes.
Interventions can be flexibly specified, both as interventions on a single
treatment or as joint interventions on multiple treatments. See McGrath et
al. (2020) <doi:10.1016/j.patter.2020.100008> for a guide on how to use
the package.

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

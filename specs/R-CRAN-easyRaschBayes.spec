%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easyRaschBayes
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Rasch Analysis Using 'brms'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-brms >= 2.20.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-ggdist 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-brms >= 2.20.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-ggdist 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Reproduces classic Rasch psychometric analysis features using Bayesian
item response theory models fitted with 'brms' following Bürkner (2021)
<doi:10.18637/jss.v100.i05> and Bürkner (2020)
<doi:10.3390/jintelligence8010005>. Supports both dichotomous and
polytomous Rasch models. Features include posterior predictive item fit,
conditional infit, item-restscore associations, person fit, differential
item functioning, local dependence assessment via Q3 residual
correlations, dimensionality assessment with residual principal components
analysis, person-item targeting plots, item category probability curves,
and reliability using relative measurement uncertainty following Bignardi
et al. (2025) <doi:10.31234/osf.io/h54k8_v1>.

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

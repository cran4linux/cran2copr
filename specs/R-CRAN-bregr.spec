%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bregr
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easy and Efficient Batch Processing of Regression Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-vctrs >= 0.5.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-broom.helpers 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forestploter 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-mirai 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-vctrs >= 0.5.0
Requires:         R-CRAN-broom 
Requires:         R-CRAN-broom.helpers 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forestploter 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-mirai 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Easily processes batches of univariate or multivariate regression models.
Returns results in a tidy format and generates visualization plots for
straightforward interpretation (Wang, Shixiang, et al. (2021)
<DOI:10.1002/mdr2.70028>).

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

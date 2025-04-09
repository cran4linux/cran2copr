%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  postcard
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Marginal Effects with Prognostic Covariate Adjustment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-options 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-workflowsets 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-yardstick 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-options 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rsample 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tune 
Requires:         R-utils 
Requires:         R-CRAN-workflowsets 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-yardstick 

%description
Conduct power analyses and inference of marginal effects. Uses plug-in
estimation and influence functions to perform robust inference, optionally
leveraging historical data to increase precision with prognostic covariate
adjustment. The methods are described in Højbjerre-Frandsen et al. (2025)
<doi:10.48550/arXiv.2503.22284>.

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

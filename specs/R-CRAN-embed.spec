%global packname  embed
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Extra Recipes for Encoding Categorical Predictors

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-recipes >= 0.1.8
BuildRequires:    R-CRAN-rstanarm 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-rsample 
Requires:         R-CRAN-recipes >= 0.1.8
Requires:         R-CRAN-rstanarm 
Requires:         R-CRAN-keras 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-rsample 

%description
Predictors can be converted to one or more numeric representations using
simple generalized linear models <arXiv:1611.09477> or nonlinear models
<arXiv:1604.06737>. Most encoding methods are supervised.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

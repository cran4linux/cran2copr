%global __brp_check_rpaths %{nil}
%global packname  tune
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Tuning Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.0
BuildRequires:    R-CRAN-cli >= 2.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-workflows >= 0.2.2
BuildRequires:    R-CRAN-parsnip >= 0.1.4
BuildRequires:    R-CRAN-recipes >= 0.1.15
BuildRequires:    R-CRAN-generics >= 0.1.0
BuildRequires:    R-CRAN-dials >= 0.0.9
BuildRequires:    R-CRAN-rsample >= 0.0.9
BuildRequires:    R-CRAN-yardstick >= 0.0.7
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-GPfit 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-tibble >= 3.1.0
Requires:         R-CRAN-cli >= 2.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-workflows >= 0.2.2
Requires:         R-CRAN-parsnip >= 0.1.4
Requires:         R-CRAN-recipes >= 0.1.15
Requires:         R-CRAN-generics >= 0.1.0
Requires:         R-CRAN-dials >= 0.0.9
Requires:         R-CRAN-rsample >= 0.0.9
Requires:         R-CRAN-yardstick >= 0.0.7
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-GPfit 
Requires:         R-CRAN-tidyr 

%description
The ability to tune models is important. 'tune' contains functions and
classes to be used in conjunction with other 'tidymodels' packages for
finding reasonable values of hyper-parameters in models, pre-processing
methods, and post-processing steps.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

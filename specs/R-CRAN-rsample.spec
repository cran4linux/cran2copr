%global __brp_check_rpaths %{nil}
%global packname  rsample
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          General Resampling Infrastructure

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-slider >= 0.1.5
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-slider >= 0.1.5
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-methods 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-lifecycle 

%description
Classes and functions to create and summarize different types of
resampling objects (e.g. bootstrap, cross-validation).

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

%global __brp_check_rpaths %{nil}
%global packname  groupdata2
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Creating Groups from Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-plyr >= 1.8.5
BuildRequires:    R-CRAN-dplyr >= 0.8.4
BuildRequires:    R-CRAN-numbers >= 0.7.5
BuildRequires:    R-CRAN-rlang >= 0.4.4
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-plyr >= 1.8.5
Requires:         R-CRAN-dplyr >= 0.8.4
Requires:         R-CRAN-numbers >= 0.7.5
Requires:         R-CRAN-rlang >= 0.4.4
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Methods for dividing data into groups. Create balanced partitions and
cross-validation folds. Perform time series windowing and general grouping
and splitting of data. Balance existing groups with up- and downsampling.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  yardstick
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Characterizations of Model Performance

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-tidyselect >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-hardhat >= 1.0.0
BuildRequires:    R-CRAN-vctrs >= 0.4.1
BuildRequires:    R-CRAN-generics >= 0.1.2
BuildRequires:    R-utils 
Requires:         R-CRAN-tidyselect >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-hardhat >= 1.0.0
Requires:         R-CRAN-vctrs >= 0.4.1
Requires:         R-CRAN-generics >= 0.1.2
Requires:         R-utils 

%description
Tidy tools for quantifying how well model fits to a data set such as
confusion matrices, class probability curve summaries, and regression
metrics (e.g., RMSE).

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  viraldomain
%global packver   0.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Applicability Domain Methods of Viral Load and CD4 Lymphocytes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-applicable 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-kknn 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-workflows 
Requires:         R-CRAN-applicable 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-kknn 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-recipes 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-workflows 

%description
Provides methods for assessing the applicability domain of models that
predict viral load and CD4 (Cluster of Differentiation 4) lymphocyte
counts. These methods help determine the extent of extrapolation when
making predictions.

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

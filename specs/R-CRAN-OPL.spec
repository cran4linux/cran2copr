%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OPL
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Policy Learning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-tidyr 

%description
Provides functions for optimal policy learning in socioeconomic
applications helping users to learn the most effective policies based on
data in order to maximize empirical welfare. Specifically, 'OPL' allows to
find "treatment assignment rules" that maximize the overall welfare,
defined as the sum of the policy effects estimated over all the policy
beneficiaries. Documentation about 'OPL' is provided by several
international articles via Athey et al (2021, <doi:10.3982/ECTA15732>),
Kitagawa et al (2018, <doi:10.3982/ECTA13288>), Cerulli (2022,
<doi:10.1080/13504851.2022.2032577>), the paper by Cerulli (2021,
<doi:10.1080/13504851.2020.1820939>) and the book by Gareth et al (2013,
<doi:10.1007/978-1-4614-7138-7>).

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

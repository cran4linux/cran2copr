%global __brp_check_rpaths %{nil}
%global packname  gesttools
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          General Purpose G-Estimation for End of Study or Time-Varying Outcomes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DataCombine 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-geeM 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-DataCombine 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-geeM 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-testthat 

%description
Provides a series of general purpose tools to perform g-estimation using
the methods described in Sjolander and Vansteelandt (2016)
<doi:10.1515/em-2015-0005> and Dukes and Vansteelandt
<doi:10.1093/aje/kwx347>. The package allows for g-estimation in a wide
variety of circumstances, including an end of study or time-varying
outcome, and an exposure that is a binary, continuous, or a categorical
variable with three or more categories. The package also supports
g-estimation with time-varying causal effects and effect modification by a
confounding variable.

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

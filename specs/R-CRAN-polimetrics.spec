%global __brp_check_rpaths %{nil}
%global packname  polimetrics
%global packver   1.2.1.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1.14
Release:          1%{?dist}%{?buildtag}
Summary:          R Tools for Political Measures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-car 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-rstatix 
Requires:         R-CRAN-stringr 

%description
This is a collection of data and functions for common metrics in political
science research. Data measuring ideology, and functions calculating
geographical diffusion and ideological diffusion - geog.diffuse() and
ideo.dist(), respectively. Functions derived from methods developed in:
Soule and King (2006) <doi:10.1086/499908>, Berry et al. (1998)
<doi:10.2307/2991759>, Cruz-Aceves and Mallinson (2019)
<doi:10.1177/0160323X20902818>, and Grossback et al. (2004)
<doi:10.1177/1532673X04263801>.

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

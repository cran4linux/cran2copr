%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyttmoment
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Trait Moment Calculation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-fundiversity 
BuildRequires:    R-CRAN-funrar 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-fundiversity 
Requires:         R-CRAN-funrar 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Calculates the community four 'moments' (mean, variance, skewness, and
kurtosis) of a given trait based on the moments described in Wieczynski et
al. (2019) <doi:10.1073/pnas.1813723116>. These functional metrics are
extremely useful in characterizing the distribution of traits in a plant
community. It also provides tidyverse-friendly wrappers to seamlessly
calculate advanced functional diversity indices (e.g., FDis, Rao's Q)
using 'fundiversity' (Grenie et al. 2023 <doi:10.1111/ecog.06585>) and
functional rarity indices using 'funrar' (Grenie et al. 2017
<doi:10.1111/ddi.12629>). Evaluating these community-weighted moments and
diversity metrics allows researchers to evaluate shifts in optimal
phenotypes and understand ecological filtering with exactness.

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

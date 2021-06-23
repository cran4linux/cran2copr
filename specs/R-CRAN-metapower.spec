%global __brp_check_rpaths %{nil}
%global packname  metapower
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analysis for Meta-Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-testthat >= 2.3.2
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-knitr >= 1.28
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-cowplot >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-testthat >= 2.3.2
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-knitr >= 1.28
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-cowplot >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.5

%description
A simple and effective tool for computing and visualizing statistical
power for meta-analysis, including power analysis of main effects (Jackson
& Turner, 2017)<doi:10.1002/jrsm.1240>, test of homogeneity (Pigott,
2012)<doi:10.1007/978-1-4614-2278-5>, subgroup analysis, and categorical
moderator analysis (Hedges & Pigott, 2004)<doi:10.1037/1082-989X.9.4.426>.

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

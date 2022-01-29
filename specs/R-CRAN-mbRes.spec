%global __brp_check_rpaths %{nil}
%global packname  mbRes
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Integrating Multiple Biomarker Responses in Aquatic Organisms using Effect Size, Statistical Uncertainty, and Ecological Relevance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-tibble >= 3.1.6
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-data.table >= 1.14.2
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-cowplot >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-forcats >= 0.5.1
BuildRequires:    R-CRAN-rlang >= 0.4.12
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-ggforce >= 0.3.3
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-tibble >= 3.1.6
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-data.table >= 1.14.2
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-cowplot >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-forcats >= 0.5.1
Requires:         R-CRAN-rlang >= 0.4.12
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-ggforce >= 0.3.3
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 

%description
Compute and visualize the ps-index, a new integrated index for multiple
biomarker responses, as described in Pham & Sokolova (2022, unpublished).

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

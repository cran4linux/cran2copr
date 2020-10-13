%global packname  BENMMI
%global packver   4.3-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Benthic Multi-Metric Index

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-benthos >= 1.3.5
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-benthos >= 1.3.5
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-readr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-tidyr 

%description
Analysis tool for evaluating benthic multimetric indices (BENMMIs). It
generates reproducible reports on the analysis of benthic data, e.g.,
validation and correction of species names, sample pooling, automatic
conversion of genus to species names, outlier detection, benthic indicator
calculation, optimization of single and multimetric indicators against a
pressure gradient, and spatial aggregation of benthic indicators. One of
its use cases was the development of a common benthic indicator for
<https://www.ospar.org> (publication accepted by Ecological Indicators).
See Van Loon et al. (2018) <doi:10.1016/j.ecolind.2017.09.029> for
details.

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

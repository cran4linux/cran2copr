%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  visvaR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Shiny-Based Statistical Solutions for Agricultural Research

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-agricolae 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-htmltools 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Visualize Variance is an intuitive 'shiny' applications tailored for
agricultural research data analysis, including one-way and two-way
analysis of variance, correlation, and other essential statistical tools.
Users can easily upload their datasets, perform analyses, and download the
results as a well-formatted document, streamlining the process of data
analysis and reporting in agricultural research.The experimental design
methods are based on classical work by Fisher (1925) and Scheffe (1959).
The correlation visualization approaches follow methods developed by Wei &
Simko (2021) and Friendly (2002) <doi:10.1198/000313002533>.

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

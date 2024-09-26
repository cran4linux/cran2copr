%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DescTools
%global packver   0.99.57
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.57
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Descriptive Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-Exact 
BuildRequires:    R-CRAN-gld 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-base 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-utils 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-Exact 
Requires:         R-CRAN-gld 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-cli 

%description
A collection of miscellaneous basic statistic functions and convenience
wrappers for efficiently describing data. The author's intention was to
create a toolbox, which facilitates the (notoriously time consuming) first
descriptive tasks in data analysis, consisting of calculating descriptive
statistics, drawing graphical summaries and reporting the results. The
package contains furthermore functions to produce documents using MS Word
(or PowerPoint) and functions to import data from Excel. Many of the
included functions can be found scattered in other packages and other
sources written partly by Titans of R. The reason for collecting them
here, was primarily to have them consolidated in ONE instead of dozens of
packages (which themselves might depend on other packages which are not
needed at all), and to provide a common and consistent interface as far as
function and arguments naming, NA handling, recycling rules etc. are
concerned. Google style guides were used as naming rules (in absence of
convincing alternatives). The 'BigCamelCase' style was consequently
applied to functions borrowed from contributed R packages as well.

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

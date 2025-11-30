%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  patternplot
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Versatile Pie Charts, Ring Charts, Bar Charts and Box Plots using Patterns, Colors and Images

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-RCurl 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Cairo 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-RCurl 

%description
Creates aesthetically pleasing and informative pie charts, ring charts,
bar charts and box plots with colors, patterns, and images.

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

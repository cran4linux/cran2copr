%global __brp_check_rpaths %{nil}
%global packname  plotROC
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generate Useful ROC Curve Charts for Print and Interactive Use

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridSVG 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-gridSVG 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rlang 

%description
Most ROC curve plots obscure the cutoff values and inhibit interpretation
and comparison of multiple curves. This attempts to address those
shortcomings by providing plotting and interactive tools. Functions are
provided to generate an interactive ROC curve plot for web use, and print
versions. A Shiny application implementing the functions is also included.

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

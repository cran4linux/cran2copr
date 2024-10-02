%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kim
%global packver   0.5.431
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.431
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolkit for Behavioral Scientists

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-remotes 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-remotes 

%description
A collection of functions for analyzing data typically collected or used
by behavioral scientists. Examples of the functions include a function
that compares groups in a factorial experimental design, a function that
conducts two-way analysis of variance (ANOVA), and a function that cleans
a data set generated by Qualtrics surveys. Some of the functions will
require installing additional package(s). Such packages and other
references are cited within the section describing the relevant functions.
Many functions in this package rely heavily on these two popular R
packages: Dowle et al. (2021)
<https://CRAN.R-project.org/package=data.table>. Wickham et al. (2021)
<https://CRAN.R-project.org/package=ggplot2>.

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

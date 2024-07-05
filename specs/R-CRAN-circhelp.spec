%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  circhelp
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Circular Analyses Helper Functions

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-patchwork 

%description
Light-weight functions for computing descriptive statistics in different
circular spaces (e.g., 2pi, 180, or 360 degrees), to handle
angle-dependent biases, pad circular data, and more. Specifically aimed
for psychologists and neuroscientists analyzing circular data. Basic
methods are based on Jammalamadaka and SenGupta (2001) <doi:10.1142/4031>,
removal of cardinal biases is based on the approach introduced in van
Bergen, Ma, Pratte, & Jehee (2015) <doi:10.1038/nn.4150> and Chetverikov
and Jehee (2023) <doi:10.1038/s41467-023-43251-w>.

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

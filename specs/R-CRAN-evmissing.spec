%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evmissing
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extreme Value Analyses with Missing Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlssx 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-itp 
BuildRequires:    R-CRAN-nieve 
BuildRequires:    R-CRAN-revdbayes 
BuildRequires:    R-CRAN-rust 
BuildRequires:    R-stats 
Requires:         R-CRAN-gamlssx 
Requires:         R-graphics 
Requires:         R-CRAN-itp 
Requires:         R-CRAN-nieve 
Requires:         R-CRAN-revdbayes 
Requires:         R-CRAN-rust 
Requires:         R-stats 

%description
Performs likelihood-based extreme value inferences with adjustment for the
presence of missing values based on Simpson and Northrop (2025)
<doi:10.48550/arXiv.2512.15429>. A Generalised Extreme Value distribution
is fitted to block maxima using maximum likelihood estimation, with the
location and scale parameters reflecting the numbers of non-missing raw
values in each block. A Bayesian version is also provided. For the
purposes of comparison, there are options to make no adjustment for
missing values or to discard any block maximum for which greater than a
percentage of the underlying raw values are missing. Example datasets
containing missing values are provided.

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

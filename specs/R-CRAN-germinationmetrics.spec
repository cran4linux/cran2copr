%global packname  germinationmetrics
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Seed Germination Indices and Curve Fitting

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-Rdpack 
Requires:         R-utils 
Requires:         R-stats 

%description
Provides functions to compute various germination indices such as
germinability, median germination time, mean germination time, mean
germination rate, speed of germination, Timson's index, germination value,
coefficient of uniformity of germination, uncertainty of germination
process, synchrony of germination etc. from germination count data.
Includes functions for fitting cumulative seed germination curves using
four-parameter hill function and computation of associated parameters. See
the vignette for more, including full list of citations for the methods
implemented.

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

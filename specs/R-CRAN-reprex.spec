%global __brp_check_rpaths %{nil}
%global packname  reprex
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Prepare Reproducible Example Code via the Clipboard

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 3.6.0
BuildRequires:    R-CRAN-cli >= 2.3.1
BuildRequires:    R-CRAN-withr >= 2.3.0
BuildRequires:    R-CRAN-knitr >= 1.23
BuildRequires:    R-CRAN-clipr >= 0.4.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-utils 
Requires:         R-CRAN-callr >= 3.6.0
Requires:         R-CRAN-cli >= 2.3.1
Requires:         R-CRAN-withr >= 2.3.0
Requires:         R-CRAN-knitr >= 1.23
Requires:         R-CRAN-clipr >= 0.4.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rstudioapi 
Requires:         R-utils 

%description
Convenience wrapper that uses the 'rmarkdown' package to render small
snippets of code to target formats that include both code and output.  The
goal is to encourage the sharing of small, reproducible, and runnable
examples on code-oriented websites, such as <https://stackoverflow.com>
and <https://github.com>, or in email. The user's clipboard is the default
source of input code and the default target for rendered output. 'reprex'
also extracts clean, runnable R code from various common formats, such as
copy/paste from an R session.

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

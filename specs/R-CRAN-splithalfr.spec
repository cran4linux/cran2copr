%global __brp_check_rpaths %{nil}
%global packname  splithalfr
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Split-Half Reliabilities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-psych >= 1.8.12
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-bcaboot >= 0.2.1
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-psych >= 1.8.12
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-bcaboot >= 0.2.1

%description
Estimates split-half reliabilities for scoring algorithms of cognitive
tasks and questionnaires. The 'splithalfr' supports researcher-provided
scoring algorithms, with six vignettes illustrating how on included
datasets. The package provides four splitting methods (first-second,
odd-even, permutated, Monte Carlo), the option to stratify splits by task
design, a number of reliability coefficients, and the option to sub-sample
data.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smartcor
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Correlation Method Selection Based on Variable Types

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-generics 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-polycor 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Detects variable types (continuous, count, binary, ordinal, categorical)
and selects the appropriate correlation method for each pair. Supports
Pearson, Spearman, Kendall's tau, point-biserial, rank-biserial, phi,
tetrachoric, polychoric, polyserial, Cramer's V, Tschuprow's T, Theil's U,
Yule's Q, and Goodman-Kruskal's gamma, each with a confidence interval and
p-value. Explains the selection rationale in the output, follows tidy data
principles, and works in both interactive and scripted workflows. The
methodology is described in Harshvardhan and Ranjan (2026)
<doi:10.48550/arXiv.2607.22285>.

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

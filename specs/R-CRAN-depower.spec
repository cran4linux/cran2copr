%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  depower
%global packver   2024.12.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2024.12.4
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analysis for Differential Expression Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-multidplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-glmmTMB 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-multidplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 

%description
Provides a convenient framework to simulate, test, power, and visualize
data for differential expression studies with lognormal or negative
binomial outcomes. Supported designs are two-sample comparisons of
independent or dependent outcomes. Power may be summarized in the context
of controlling the per-family error rate or family-wise error rate.
Negative binomial methods are described in Yu, Fernandez, and Brock (2017)
<doi:10.1186/s12859-017-1648-2> and Yu, Fernandez, and Brock (2020)
<doi:10.1186/s12859-020-3541-7>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fewclust
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Regression for Clustered Binary Outcomes with Few Clusters

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-generics 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Fits regression models for binary outcomes measured repeatedly within a
small number of groups (clusters), with tests and intervals that stay
calibrated with few groups and short series.  The default is the
marginalized multilevel model of Heagerty (1999)
<doi:10.1111/j.0006-341X.1999.00688.x> with a convergence check and Wald
statistics referred to a t distribution; generalized estimating equations
with a first-order autoregressive working correlation and the small-sample
sandwich correction of Fay and Graubard (2001)
<doi:10.1111/j.0006-341X.2001.01198.x> are the fallback.  The corrections
of Mancl and DeRouen (2001) <doi:10.1111/j.0006-341X.2001.00126.x> and
Kauermann and Carroll (2001) <doi:10.1198/016214501753382309> are
available, and the sign-flip score test of Hemerik, Goeman and Finos
(2020) <doi:10.1111/rssb.12369> gives a p-value for the smallest designs.
The defaults follow a simulation study of these methods.  Fits take the
data first, accept bare column names and have 'broom' methods returning
tibbles.

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

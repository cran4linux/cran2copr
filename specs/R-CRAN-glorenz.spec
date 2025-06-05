%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glorenz
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Transformed and Relative Lorenz Curves for Survey Weighted Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-LorenzRegression 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-LorenzRegression 
Requires:         R-CRAN-rlang 

%description
Functions for constructing Transformed and Relative Lorenz curves with
survey sampling weights. Given a variable of interest measured in two
groups with scaled survey weights so that their hypothetical populations
are of equal size, tlorenz() computes the proportion of members of the
group with smaller values (ordered from smallest to largest) needed for
their sum to match the sum of the top qth percentile of the group with
higher values. rlorenz() shows the fraction of the total value of the
group with larger values held by the pth percentile of those in the group
with smaller values. Fd() is a survey weighted cumulative distribution
function and Eps() is a survey weighted inverse cdf used in rlorenz().
Ramos, Graubard, and Gastwirth (2025) <doi:10.1093/jrsssa/qnaf044>.

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

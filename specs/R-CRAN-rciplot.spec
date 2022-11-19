%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rciplot
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plot Jacobson-Truax Reliable Change Indices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
The concept of reliable and clinically significant change (Jacobson &
Truax, 1991) helps you answer the following questions for a sample with
two measurements at different points in time (pre & post): Which
proportion of my sample has a (considering the reliability of the
instrument) probably not-just-by-chance difference in pre- vs.
post-scores? Which proportion of my sample does not only change in a
statistically significant way (see question one), but also in a clinically
significant way (e.g. change from a test score regarded "dysfunctional" to
a score regarded "functional")? This package allows you to very easily
create a scatterplot of your sample in which the x-axis maps to the
pre-scores, the y-axis maps to the post-scores and several graphical
elements (lines, colors) allow you to gain a quick overview about reliable
changes in these scores. An example of this kind of plot is Figure 2 of
Jacobson & Truax (1991). Referenced article: Jacobson, N. S., & Truax, P.
(1991) <doi:10.1037/0022-006X.59.1.12>.

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

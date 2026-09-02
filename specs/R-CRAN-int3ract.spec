%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  int3ract
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Johnson-Neyman Analysis of Two- and Three-Way Interactions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpattern 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpattern 
Requires:         R-CRAN-patchwork 

%description
Reports and plots the conditional effect of each variable involved in a
multiplicative interaction across the range of its moderators, together
with the region over which that effect is distinguishable from zero.
Extends the classic framework of Johnson and Neyman (1936) and Johnson and
Fay (1950) <doi:10.1007/BF02288864> to three-way interactions and to
Bayesian models. The single entry point JN() dispatches on the fitted
object, with methods for lm()/glm() models, 'lme4' models, 'RSiena' and
'multiSiena' results, and matrices of posterior draws; support for further
model classes is added by writing one jn_input() method. Results are
classed objects with print(), summary() and plot() methods, and the
figures carry data-density panels showing how much empirical support each
part of the moderator range has. A detailed introduction can be found in
Krause (2026) <doi:10.48550/arXiv.2604.22051>.

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

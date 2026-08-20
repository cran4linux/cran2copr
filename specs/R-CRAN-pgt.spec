%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pgt
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Envelopment Analysis for Pollution-Generating Technologies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lpSolveAPI 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-lpSolveAPI 

%description
Nonparametric efficiency analysis for pollution-generating technologies
under the materials-balance principle. Implements the weak-G-disposability
model of Rodseth (2025) <doi:10.1007/s11123-025-00768-0> and its
factorially determined multi-output representation, the by-production
intersection technology of Murty, Russell and Levkoff (2012)
<doi:10.1016/j.jeem.2012.02.005>, the materials-balance cost model of
Coelli, Lauwers and Van Huylenbroeck (2007)
<doi:10.1007/s11123-007-0052-8> and a weak-disposability reference model,
with an enforced materials-balance identity, a pre-estimation feasibility
audit, metafrontier decompositions, bad-output shadow prices, marginal
abatement cost curves, a cross-axiom comparison harness, a global
Malmquist-Luenberger productivity index and subsampling inference.
Estimators are solved with 'lpSolveAPI'.

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

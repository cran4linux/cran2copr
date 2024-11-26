%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  serp
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Smooth Effects on Response Penalty for CLM

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ordinal >= 2016.12.12
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-stats 
Requires:         R-CRAN-ordinal >= 2016.12.12
Requires:         R-CRAN-crayon 
Requires:         R-stats 

%description
Implements a regularization method for cumulative link models using the
Smooth-Effect-on-Response Penalty (SERP). This method allows flexible
modeling of ordinal data by enabling a smooth transition from a general
cumulative link model to a simplified version of the same model. As the
tuning parameter increases from zero to infinity, the subject-specific
effects for each variable converge to a single global effect. The approach
addresses common issues in cumulative link models, such as parameter
unidentifiability and numerical instability, by maximizing a penalized
log-likelihood instead of the standard non-penalized version. Fitting is
performed using a modified Newton's method. Additionally, the package
includes various model performance metrics and descriptive tools. For
details on the implemented penalty method, see Ugba (2021)
<doi:10.21105/joss.03705> and Ugba et al. (2021)
<doi:10.3390/stats4030037>.

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

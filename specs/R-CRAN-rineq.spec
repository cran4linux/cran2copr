%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rineq
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Concentration Index and Decomposition for Health Inequalities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Relative, generalized, and Erreygers corrected concentration index; plot
Lorenz curves; and decompose health inequalities into contributing
factors. The package currently works with (generalized) linear models,
survival models, complex survey models, and marginal effects probit
models. originally forked by Brecht Devleesschauwer from the 'decomp'
package (no longer on CRAN), 'rineq' is now maintained by Kaspar Walter
Meili. Compared to the earlier 'rineq' version on 'github' by Brecht
Devleesschauwer (<https://github.com/brechtdv/rineq>), the regression tree
functionality has been removed. Improvements compared to earlier versions
include improved plotting of decomposition and concentration, added
functionality to calculate the concentration index with different methods,
calculation of robust standard errors, and support for the decomposition
analysis using marginal effects probit regression models. The development
version is available at <https://github.com/kdevkdev/rineq>.

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

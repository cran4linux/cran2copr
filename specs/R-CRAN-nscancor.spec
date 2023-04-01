%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nscancor
%global packver   0.7.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Negative and Sparse CCA

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-stats 

%description
Two implementations of canonical correlation analysis (CCA) that are based
on iterated regression. By choosing the appropriate regression algorithm
for each data domain, it is possible to enforce sparsity, non-negativity
or other kinds of constraints on the projection vectors. Multiple
canonical variables are computed sequentially using a generalized
deflation scheme, where the additional correlation not explained by
previous variables is maximized. nscancor() is used to analyze paired data
from two domains, and has the same interface as cancor() from the 'stats'
package (plus some extra parameters). mcancor() is appropriate for
analyzing data from three or more domains. See
<https://sigg-iten.ch/learningbits/2014/01/20/canonical-correlation-analysis-under-constraints/>
and Sigg et al. (2007) <doi:10.1109/MLSP.2007.4414315> for more details.

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

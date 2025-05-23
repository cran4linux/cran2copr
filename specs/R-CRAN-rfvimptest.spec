%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rfvimptest
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Permutation Testing of Random Forest Variable Importance Measures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-permimp 
Requires:         R-CRAN-party 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-permimp 

%description
Sequential permutation testing for statistical significance of predictors
in random forests and other prediction methods. The main function of the
package is rfvimptest(), which allows to test for the statistical
significance of predictors in random forests using different (sequential)
permutation test strategies [1]. The advantage of sequential over
conventional permutation tests is that they are computationally
considerably less intensive, as the sequential procedure is stopped as
soon as there is sufficient evidence for either the null or the
alternative hypothesis. Reference: [1] Hapfelmeier, A., Hornung, R. &
Haller, B. (2023) Efficient permutation testing of variable importance
measures by the example of random forests. Computational Statistics & Data
Analysis 181:107689, <doi:10.1016/j.csda.2022.107689>.

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

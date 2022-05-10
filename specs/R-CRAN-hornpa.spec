%global __brp_check_rpaths %{nil}
%global packname  hornpa
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Horn's (1965) Test to Determine the Number of Components/Factors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A stand-alone function that generates a user specified number of random
datasets and computes eigenvalues using the random datasets (i.e.,
implements Horn's [1965, Psychometrika] parallel analysis
<https://link.springer.com/article/10.1007/BF02289447>). Users then
compare the resulting eigenvalues (the mean or the specified percentile)
from the random datasets (i.e., eigenvalues resulting from noise) to the
eigenvalues generated with the user's data. Can be used for both principal
components analysis (PCA) and common/exploratory factor analysis (EFA).
The output table shows how large eigenvalues can be as a result of merely
using randomly generated datasets. If the user's own dataset has actual
eigenvalues greater than the corresponding eigenvalues, that lends support
to retain that factor/component. In other words, if the i(th) eigenvalue
from the actual data was larger than the percentile of the (i)th
eigenvalue generated using randomly generated data, empirical support is
provided to retain that factor/component. Horn, J. (1965). A rationale and
test for the number of factors in factor analysis. Psychometrika, 32,
179-185.

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

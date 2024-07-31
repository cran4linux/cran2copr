%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drglm
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Linear and Generalized Linear Models in "Divide and Recombine" Approach to Large Data Sets

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-speedglm 
BuildRequires:    R-stats 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-speedglm 
Requires:         R-stats 

%description
To overcome the memory limitations for fitting linear (LM) and Generalized
Linear Models (GLMs) to large data sets, this package implements the
Divide and Recombine (D&R) strategy. It basically divides the entire large
data set into suitable subsets manageable in size and then fits model to
each subset. Finally, results from each subset are aggregated to obtain
the final estimate. This package also supports fitting GLMs to data sets
that cannot fit into memory and provides methods for fitting GLMs under
linear regression, binomial regression, Poisson regression, and
multinomial logistic regression settings. Respective models are fitted
using different D&R strategies as described by: Xi, Lin, and Chen (2009)
<doi:10.1109/TKDE.2008.186>, Xi, Lin and Chen (2006)
<doi:10.1109/TKDE.2006.196>, Zuo and Li (2018)
<doi:10.4236/ojs.2018.81003>, Karim, M.R., Islam, M.A. (2019)
<doi:10.1007/978-981-13-9776-9>.

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

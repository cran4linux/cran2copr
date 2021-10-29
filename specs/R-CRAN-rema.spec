%global __brp_check_rpaths %{nil}
%global packname  rema
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Rare Event Meta Analysis

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-progress 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 

%description
The rema package implements a permutation-based approach for binary
meta-analyses of 2x2 tables, founded on conditional logistic regression,
that provides more reliable statistical tests when heterogeneity is
observed in rare event data (Zabriskie et al. 2021
<doi:10.1002/sim.9142>). To adjust for the effect of heterogeneity, this
method conditions on the sufficient statistic of a proxy for the
heterogeneity effect as opposed to estimating the heterogeneity variance.
While this results in the model not strictly falling under the
random-effects framework, it is akin to a random-effects approach in that
it assumes differences in variability due to treatment. Further, this
method does not rely on large-sample approximations or continuity
corrections for rare event data. This method uses the permutational
distribution of the test statistic instead of asymptotic approximations
for inference. The number of observed events drives the computation
complexity for creating this permutational distribution. Accordingly, for
this method to be computationally feasible, it should only be applied to
meta-analyses with a relatively low number of observed events. To create
this permutational distribution, a network algorithm, based on the work of
Mehta et al. (1992) <doi:10.2307/1390598> and Corcoran et al. (2001)
<doi:10.1111/j.0006-341x.2001.00941.x>, is employed using C++ and
integrated into the package.

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

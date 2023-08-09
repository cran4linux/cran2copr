%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bvpa
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bivariate Pareto Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 

%description
Implements the EM algorithm with one-step Gradient Descent method to
estimate the parameters of the Block-Basu bivariate Pareto distribution
with location and scale. We also found parametric bootstrap and asymptotic
confidence intervals based on the observed Fisher information of scale and
shape parameters, and exact confidence intervals for location parameters.
Details are in Biplab Paul and Arabin Kumar Dey (2023)
<doi:10.48550/arXiv.1608.02199> "An EM algorithm for absolutely continuous
Marshall-Olkin bivariate Pareto distribution with location and scale"; E L
Lehmann and George Casella (1998) <doi:10.1007/b98854> "Theory of Point
Estimation"; Bradley Efron and R J Tibshirani (1994)
<doi:10.1201/9780429246593> "An Introduction to the Bootstrap"; A P
Dempster, N M Laird and D B Rubin (1977) <www.jstor.org/stable/2984875>
"Maximum Likelihood from Incomplete Data via the EM Algorithm".

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

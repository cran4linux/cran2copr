%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AIPW
%global packver   0.6.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Augmented Inverse Probability Weighting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-Rsolnp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-Rsolnp 

%description
The 'AIPW' package implements the augmented inverse probability weighting,
a doubly robust estimator, for average causal effect estimation with
user-defined stacked machine learning algorithms. To cite the 'AIPW'
package, please use: "Yongqi Zhong, Edward H. Kennedy, Lisa M. Bodnar,
Ashley I. Naimi (2021). AIPW: An R Package for Augmented Inverse
Probability Weighted Estimation of Average Causal Effects. American
Journal of Epidemiology. <doi:10.1093/aje/kwab207>". Visit:
<https://yqzhong7.github.io/AIPW/> for more information.

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

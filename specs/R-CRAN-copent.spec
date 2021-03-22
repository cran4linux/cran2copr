%global packname  copent
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Copula Entropy and Transfer Entropy

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
The nonparametric methods for estimating copula entropy and transfer
entropy are implemented. The method for estimating copula entropy composes
of two simple steps: estimating empirical copula by rank statistic and
estimating copula entropy with k-Nearest-Neighbour method. The method for
estimating transfer entropy composes of two steps: estimating three copula
entropy terms and then calculate transfer entropy from the estimated
copula entropy terms. Copula Entropy is a mathematical concept for
multivariate statistical independence measuring and testing, and proved to
be equivalent to mutual information. Estimating copula entropy can be
applied to many cases, including but not limited to variable selection and
causal discovery (by estimating transfer entropy). Please refer to Ma and
Sun (2011) <doi:10.1016/S1007-0214(11)70008-6> and Ma (2019)
<arXiv:1910.04375> for more information.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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

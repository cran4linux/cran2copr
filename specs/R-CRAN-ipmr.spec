%global packname  ipmr
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fits Integral Projection Models Using an Expression Based Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-purrr >= 0.3.0
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
Flexibly implements Integral Projection Models using an expression based
framework. This will not abstract away the model selection process, but it
will make sure you get everything after that correct. It handles density
dependence and environmental stochasticity, with a couple of options for
implementing the latter. In addition, provides functions to avoid
unintentional eviction of individuals from models. Additionally, provides
model diagnostic tools, plotting functionality, stochastic/deterministic
simulations, and analysis tools. Integral projection models are described
in depth by Easterling et al. (2000)
<doi:10.1890/0012-9658(2000)081[0694:SSSAAN]2.0.CO;2>, Merow et al. (2013)
<doi:10.1111/2041-210X.12146>, Rees et al. (2014)
<doi:10.1111/1365-2656.12178>, and Metcalf et al. (2015)
<doi:10.1111/2041-210X.12405>. Williams et al. (2012)
<doi:10.1890/11-2147.1> discuss the problem of unintentional eviction.

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

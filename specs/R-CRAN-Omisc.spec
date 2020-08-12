%global packname  Omisc
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Univariate Bootstrapping and Other Things

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-copula 
Requires:         R-MASS 
Requires:         R-base 
Requires:         R-stats 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-copula 

%description
Primarily devoted to implementing the Univariate Bootstrap (as well as the
Traditional Bootstrap). In addition there are multiple functions for
DeFries-Fulker behavioral genetics models. The univariate bootstrapping
functions, DeFries-Fulker functions, regression and traditional
bootstrapping functions form the original core. Additional features may
come online later, however this software is a work in progress. For more
information about univariate bootstrapping see: Lee and Rodgers (1998) and
Beasley et al (2007) <doi.org/10.1037/1082-989X.12.4.414>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

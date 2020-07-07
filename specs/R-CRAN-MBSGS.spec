%global packname  MBSGS
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Multivariate Bayesian Sparse Group Selection with Spike and Slab

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-MASS 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-CRAN-MCMCpack 
Requires:         R-MASS 
Requires:         R-mgcv 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-truncnorm 

%description
An implementation of a Bayesian sparse group model using spike and slab
priors in a regression context. It is designed for regression with a
multivariate response variable, but also provides an implementation for
univariate response.

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

%files
%{rlibdir}/%{packname}

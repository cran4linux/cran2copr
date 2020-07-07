%global packname  glmm
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          2%{?dist}
Summary:          Generalized Linear Mixed Models via Monte Carlo LikelihoodApproximation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-trust 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-itertools 
BuildRequires:    R-utils 
Requires:         R-CRAN-trust 
Requires:         R-CRAN-mvtnorm 
Requires:         R-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-stats 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-itertools 
Requires:         R-utils 

%description
Approximates the likelihood of a generalized linear mixed model using
Monte Carlo likelihood approximation. Then maximizes the likelihood
approximation to return maximum likelihood estimates, observed Fisher
information, and other model information.

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

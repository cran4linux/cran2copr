%global packname  mvst
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Bayesian Inference for the Multivariate Skew-t Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mnormt 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mnormt 

%description
Estimates the multivariate skew-t and nested models, as described in the
articles Liseo, B., Parisi, A. (2013). Bayesian inference for the
multivariate skew-normal model: a population Monte Carlo approach. Comput.
Statist. Data Anal. <doi:10.1016/j.csda.2013.02.007> and in Parisi, A.,
Liseo, B. (2017). Objective Bayesian analysis for the multivariate skew-t
model. Statistical Methods & Applications <doi:
10.1007/s10260-017-0404-0>.

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

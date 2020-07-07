%global packname  EasyABC
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          2%{?dist}
Summary:          Efficient Approximate Bayesian Computation Sampling Schemes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-abc 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-tensorA 
Requires:         R-CRAN-abc 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-mnormt 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-tensorA 

%description
Enables launching a series of simulations of a computer code from the R
session, and to retrieve the simulation outputs in an appropriate format
for post-processing treatments. Five sequential sampling schemes and three
coupled-to-MCMC schemes are implemented.

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

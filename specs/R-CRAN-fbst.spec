%global __brp_check_rpaths %{nil}
%global packname  fbst
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          The Full Bayesian Evidence Test, Full Bayesian Significance Test and the e-Value

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bayestestR 
BuildRequires:    R-methods 
Requires:         R-CRAN-bayestestR 
Requires:         R-methods 

%description
Provides access to a range of functions for computing and visualizing the
Full Bayesian Significance Test (FBST) and the e-value for testing a sharp
hypothesis against its alternative, and the Full Bayesian Evidence Test
(FBET) and the (generalized) Bayesian evidence value for testing a
composite (or interval) hypothesis against its alternative. The methods
are widely applicable as long as a posterior MCMC sample is available. For
details on the computation and theory of the FBST see <arXiv:2005.13181>.

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

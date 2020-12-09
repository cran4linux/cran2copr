%global packname  vICC
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Varying Intraclass Correlation Coefficients

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.10
BuildRequires:    R-CRAN-coda >= 0.19.4
BuildRequires:    R-CRAN-Rdpack >= 0.11
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
Requires:         R-CRAN-rjags >= 4.10
Requires:         R-CRAN-coda >= 0.19.4
Requires:         R-CRAN-Rdpack >= 0.11
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-nlme 

%description
Compute group-specific intraclass correlation coefficients, Bayesian
testing of homogenous within-group variance, and spike-and-slab model
selection to determine which groups share a common within-group variance
in a one-way random effects model <10.31234/osf.io/hpq7w>.

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

%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bizicount
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bivariate Zero-Inflated Count Models Using Copulas

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.54
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1.1
BuildRequires:    R-CRAN-texreg >= 1.37.5
BuildRequires:    R-CRAN-Formula >= 1.2.4
BuildRequires:    R-CRAN-pbivnorm >= 0.6.0
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-DHARMa >= 0.3.4
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-MASS >= 7.3.54
Requires:         R-CRAN-numDeriv >= 2016.8.1.1
Requires:         R-CRAN-texreg >= 1.37.5
Requires:         R-CRAN-Formula >= 1.2.4
Requires:         R-CRAN-pbivnorm >= 0.6.0
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-DHARMa >= 0.3.4
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Maximum likelihood estimation of copula-based zero-inflated (and
non-inflated) Poisson and negative binomial count models. Supports Frank
and Gaussian copulas. Allows for mixed margins (e.g., one margin Poisson,
the other zero-inflated negative binomial), and several marginal link
functions. Built-in methods for publication-quality tables using 'texreg',
post-estimation diagnostics using 'DHARMa', and testing for marginal
zero-modification via <doi:10.1177/0962280217749991>. For information on
copula regression for count data, see Genest and Nešlehová (2007)
<doi:10.1017/S0515036100014963> as well as Nikoloulopoulos (2013)
<doi:10.1007/978-3-642-35407-6_11>. For information on zero-inflated count
regression generally, see Lambert (1992)
<https:www.jstor.org/stable/1269547?origin=crossref>. The author
acknowledges support by NSF DMS-1925119 and DMS-212324.

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

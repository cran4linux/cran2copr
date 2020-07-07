%global packname  mnormt
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          2%{?dist}
Summary:          The Multivariate Normal and t Distributions, and Their TruncatedVersions

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-tmvnsim >= 1.0.2
Requires:         R-CRAN-tmvnsim >= 1.0.2

%description
Functions are provided for computing the density and the distribution
function of d-dimensional normal and "t" random variables, possibly
truncated (on one side or two sides, with componentwise choice), and for
generating random vectors sampled from these distributions, except
sampling from the truncated "t". Moments of arbitrary order of a truncated
normal are computed, and converted to cumulants up to order 4.
Probabilities are computed via non-Monte Carlo methods; different routines
are used in the case d=1, d=2, d=3, d>3, if d denotes the dimensionality.

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

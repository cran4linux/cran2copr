%global __brp_check_rpaths %{nil}
%global packname  MVTests
%global packver   2.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Hypothesis Tests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-mvtnorm 

%description
Multivariate hypothesis tests and the confidence intervals. It can be used
to test the hypothesizes about mean vector or vectors (one-sample, two
independent samples, paired samples), covariance matrix (one or more
matrices), and the correlation matrix. Moreover, it can be used for robust
Hotelling T^2 test at one sample case in high dimensional data. For this
package, we have benefited from the studies Rencher (2003), Nel and Merwe
(1986) <DOI: 10.1080/03610928608829342>, Tatlidil (1996), Tsagris (2014),
Villasenor Alva and Estrada (2009) <DOI: 10.1080/03610920802474465>.

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

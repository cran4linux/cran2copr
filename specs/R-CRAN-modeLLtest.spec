%global __brp_check_rpaths %{nil}
%global packname  modeLLtest
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Compare Models with Cross-Validated Log-Likelihood

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-coxrobust 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-CRAN-quantreg 
Requires:         R-survival 
Requires:         R-CRAN-coxrobust 
Requires:         R-MASS 
Requires:         R-CRAN-Rcpp 

%description
An implementation of the cross-validated difference in means (CVDM) test
by Desmarais and Harden (2014) <doi:10.1007/s11135-013-9884-7> (see also
Harden and Desmarais, 2011 <doi:10.1177/1532440011408929>) and the
cross-validated median fit (CVMF) test by Desmarais and Harden (2012)
<doi:10.1093/pan/mpr042>. These tests use leave-one-out cross-validated
log-likelihoods to assist in selecting among model estimations. You can
also utilize data from Golder (2010) <doi:10.1177/0010414009341714> and
Joshi & Mason (2008) <doi:10.1177/0022343308096155> that are included to
facilitate examples from real-world analysis.

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

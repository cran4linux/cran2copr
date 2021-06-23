%global __brp_check_rpaths %{nil}
%global packname  condTruncMVN
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Truncated Multivariate Normal Distribution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-condMVNorm >= 2020
BuildRequires:    R-CRAN-tmvtnorm >= 1.4.10
BuildRequires:    R-CRAN-truncnorm >= 1.0.8
BuildRequires:    R-CRAN-tmvmixnorm >= 1.0.2
BuildRequires:    R-CRAN-matrixNormal >= 0.0.1
Requires:         R-CRAN-condMVNorm >= 2020
Requires:         R-CRAN-tmvtnorm >= 1.4.10
Requires:         R-CRAN-truncnorm >= 1.0.8
Requires:         R-CRAN-tmvmixnorm >= 1.0.2
Requires:         R-CRAN-matrixNormal >= 0.0.1

%description
Computes the density and probability for the conditional truncated
multivariate normal (Horrace (2005) p. 4,
<doi:10.1016/j.jmva.2004.10.007>). Also draws random samples from this
distribution.

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

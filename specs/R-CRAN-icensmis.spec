%global __brp_check_rpaths %{nil}
%global packname  icensmis
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Study Design and Data Analysis in the Presence of Error-Prone Diagnostic Tests and Self-Reported Outcomes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
Requires:         R-CRAN-Rcpp >= 0.11.3

%description
We consider studies in which information from error-prone diagnostic tests
or self-reports are gathered sequentially to determine the occurrence of a
silent event. Using a likelihood-based approach incorporating the
proportional hazards assumption, we provide functions to estimate the
survival distribution and covariate effects. We also provide functions for
power and sample size calculations for this setting. Please refer to
Xiangdong Gu, Yunsheng Ma, and Raji Balasubramanian (2015) <doi:
10.1214/15-AOAS810>, Xiangdong Gu and Raji Balasubramanian (2016) <doi:
10.1002/sim.6962>, Xiangdong Gu, Mahlet G Tadesse, Andrea S Foulkes,
Yunsheng Ma, and Raji Balasubramanian (2020) <doi:
10.1186/s12911-020-01223-w>.

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

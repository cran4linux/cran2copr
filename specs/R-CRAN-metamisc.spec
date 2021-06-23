%global __brp_check_rpaths %{nil}
%global packname  metamisc
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Analysis of Diagnosis and Prognosis Research Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-metafor >= 2.0.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-metafor >= 2.0.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-plyr 
Requires:         R-methods 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-ggplot2 

%description
Facilitate meta-analysis of diagnosis and prognosis research studies. It
includes functions to summarize multiple estimates of prediction model
discrimination and calibration performance, as described by Debray et al.
(2019) <doi:10.1177/0962280218785504>. It also includes functions to
evaluate funnel plot asymmetry, as described by Debray et al. (2018)
<doi:10.1002/jrsm.1266>. Finally, the package provides functions for
developing multivariable prediction models from datasets with clustering.

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

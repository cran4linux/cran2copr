%global __brp_check_rpaths %{nil}
%global packname  cdcatR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Cognitive Diagnostic Computerized Adaptive Testing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-GDINA >= 2.2.0
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-NPCD 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-GDINA >= 2.2.0
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-NPCD 
Requires:         R-stats 

%description
Provides a set of functions for conducting cognitive diagnostic
computerized adaptive testing applications (Chen (2009)
<doi:10.1007/s11336-009-9123-2>). It includes different item selection
rules such us the global discrimination index (Kaplan, de la Torre, and
Barrada (2015) <doi:10.1177/0146621614554650>) and the nonparametric
selection method (Chang, Chiu, and Tsai (2019)
<doi:10.1177/0146621618813113>), as well as several stopping rules.
Functions for generating item banks and responses are also provided. To
guide item bank calibration, model comparison at the item level can be
conducted using the two-step likelihood ratio test statistic by Sorrel, de
la Torre, Abad and Olea (2017) <doi:10.1027/1614-2241/a000131>.

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

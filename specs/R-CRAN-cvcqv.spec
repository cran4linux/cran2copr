%global __brp_check_rpaths %{nil}
%global packname  cvcqv
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}%{?buildtag}
Summary:          Coefficient of Variation (CV) with Confidence Intervals (CI)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-SciViews 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-MBESS 
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-R6 
Requires:         R-CRAN-SciViews 
Requires:         R-boot 
Requires:         R-CRAN-MBESS 

%description
Provides some easy-to-use functions and classes to calculate variability
measures such as coefficient of variation with confidence intervals
provided with all available methods. References are Panichkitkosolkul
(2013) <doi:10.1155/2013/324940> , Altunkaynak & Gamgam (2018)
<doi:10.1080/03610918.2018.1435800> , Albatineh, Kibria, Wilcox & Zogheib
(2014) <doi:10.1080/02664763.2013.847405> .

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

%files
%{rlibdir}/%{packname}

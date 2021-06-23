%global __brp_check_rpaths %{nil}
%global packname  multilevelPSA
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          2%{?dist}%{?buildtag}
Summary:          Multilevel Propensity Score Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-PSAgraphics 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-PSAgraphics 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-reshape 
Requires:         R-grid 
Requires:         R-CRAN-party 
Requires:         R-MASS 

%description
Conducts and visualizes propensity score analysis for multilevel, or
clustered data. Bryer & Pruzek (2011) <doi:10.1080/00273171.2011.636693>.

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

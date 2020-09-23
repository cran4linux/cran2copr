%global packname  SDCNway
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Evaluate Disclosure Risk

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-plyr >= 1.8.5
BuildRequires:    R-CRAN-dplyr >= 0.8.4
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-methods 
Requires:         R-MASS >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-plyr >= 1.8.5
Requires:         R-CRAN-dplyr >= 0.8.4
Requires:         R-CRAN-Rdpack 
Requires:         R-methods 

%description
Tools for calculating disclosure risk measures, including record-level
measures primarily using exhaustive tabulation, as well as file-level
measures using a loglinear model. Funded by the National Center for
Education Statistics. See El Emam (2011) <doi:10.1186/gm239> for a
description of risk measures.

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

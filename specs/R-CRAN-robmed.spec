%global packname  robmed
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          (Robust) Mediation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.36
BuildRequires:    R-CRAN-sn >= 1.5.4
BuildRequires:    R-boot >= 1.3.20
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-CRAN-robustbase >= 0.92.7
BuildRequires:    R-CRAN-ggplot2 >= 0.9.3
BuildRequires:    R-methods 
Requires:         R-CRAN-quantreg >= 5.36
Requires:         R-CRAN-sn >= 1.5.4
Requires:         R-boot >= 1.3.20
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-CRAN-robustbase >= 0.92.7
Requires:         R-CRAN-ggplot2 >= 0.9.3
Requires:         R-methods 

%description
Perform mediation analysis via a (fast and robust) bootstrap test.

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

%global packname  presize
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Precision Based Sample Size Calculation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-kappaSize >= 1.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
Requires:         R-CRAN-kappaSize >= 1.2
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 

%description
Bland (2009) <doi:10.1136/bmj.b3985> recommended to base study sizes on
the width of the confidence interval rather the power of a statistical
test. The goal of 'presize' is to provide functions for such precision
based sample size calculations. For a given sample size, the functions
will return the precision (width of the confidence interval), and vice
versa.

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

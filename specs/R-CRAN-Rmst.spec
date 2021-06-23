%global __brp_check_rpaths %{nil}
%global packname  Rmst
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Computerized Adaptive Multistage Testing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rata 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-Rirt 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rata 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-Rirt 
Requires:         R-stats 

%description
Assemble the panels of computerized adaptive multistage testing by the
bottom-up and the top-down approach, and simulate the administration of
the assembled panels. The full documentation and tutorials are at
<https://github.com/xluo11/Rmst>. Reference: Luo and Kim (2018)
<doi:10.1111/jedm.12174>.

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

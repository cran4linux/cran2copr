%global __brp_check_rpaths %{nil}
%global packname  lmmpar
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Parallel Linear Mixed Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-bigmemory 
Requires:         R-MASS 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-bigmemory 

%description
Embarrassingly Parallel Linear Mixed Model calculations spread across
local cores which repeat until convergence.

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

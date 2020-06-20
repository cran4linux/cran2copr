%global packname  gimme
%global packver   0.7-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}
Summary:          Group Iterative Multiple Model Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-imputeTS >= 3.0
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-CRAN-MIIVsem >= 0.5.4
BuildRequires:    R-CRAN-lavaan >= 0.5.19
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-imputeTS >= 3.0
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-CRAN-MIIVsem >= 0.5.4
Requires:         R-CRAN-lavaan >= 0.5.19
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-nloptr 
Requires:         R-graphics 
Requires:         R-stats 

%description
Automated identification and estimation of group- and individual-level
relations in time series data from within a structural equation modeling
framework.

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

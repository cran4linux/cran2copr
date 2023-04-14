%global __brp_check_rpaths %{nil}
%global packname  offlineChange
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Detect Multiple Change Points from Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 

%description
Detect the number and locations of change points. The locations can be
either exact or in terms of ranges, depending on the available
computational resource. The method is based on Jie Ding, Yu Xiang, Lu
Shen, Vahid Tarokh (2017) <doi:10.1109/TSP.2017.2711558>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

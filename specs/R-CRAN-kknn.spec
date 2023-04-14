%global __brp_check_rpaths %{nil}
%global packname  kknn
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Weighted k-Nearest Neighbors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-igraph >= 1.0
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-igraph >= 1.0
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-graphics 

%description
Weighted k-Nearest Neighbors for Classification, Regression and
Clustering.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

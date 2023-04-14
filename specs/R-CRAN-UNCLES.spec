%global __brp_check_rpaths %{nil}
%global packname  UNCLES
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Unification of Clustering Results from Multiple Datasets usingExternal Specifications

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-kohonen 
BuildRequires:    R-class 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-kohonen 
Requires:         R-class 

%description
Consensus clustering by the unification of clustering results from
multiple datasets using external specifications.

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

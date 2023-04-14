%global __brp_check_rpaths %{nil}
%global packname  pencopulaCond
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Estimating Non-Simplified Vine Copulas Using Penalized Splines

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-pacotest 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-TSP 
BuildRequires:    R-CRAN-igraph 
Requires:         R-lattice 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-pacotest 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-TSP 
Requires:         R-CRAN-igraph 

%description
Estimating Non-Simplified Vine Copulas Using Penalized Splines.

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

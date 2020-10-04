%global packname  penDvine
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          3%{?dist}%{?buildtag}
Summary:          Flexible Pair-Copula Estimation in D-Vines using BivariatePenalized Splines

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-TSP 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-lattice 
Requires:         R-CRAN-TSP 
Requires:         R-CRAN-fda 
Requires:         R-Matrix 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-doParallel 

%description
Flexible Pair-Copula Estimation in D-vines using Bivariate Penalized
Splines.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

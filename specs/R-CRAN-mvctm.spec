%global packname  mvctm
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}
Summary:          Multivariate Variance Components Tests for Multilevel Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-MNM 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-Rfit 
BuildRequires:    R-CRAN-SpatialNP 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-MNM 
Requires:         R-nlme 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-Rfit 
Requires:         R-CRAN-SpatialNP 

%description
Permutation tests for variance components for 2-level, 3-level and 4-level
data with univariate or multivariate responses.

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

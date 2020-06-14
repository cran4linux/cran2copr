%global packname  systemfit
%global packver   1.1-24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.24
Release:          2%{?dist}
Summary:          Estimating Systems of Simultaneous Equations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich >= 2.2.9
BuildRequires:    R-stats >= 2.14.0
BuildRequires:    R-CRAN-car >= 2.0.0
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-sandwich >= 2.2.9
Requires:         R-stats >= 2.14.0
Requires:         R-CRAN-car >= 2.0.0
Requires:         R-Matrix 
Requires:         R-CRAN-lmtest 
Requires:         R-MASS 
Requires:         R-methods 

%description
Econometric estimation of simultaneous systems of linear and nonlinear
equations using Ordinary Least Squares (OLS), Weighted Least Squares
(WLS), Seemingly Unrelated Regressions (SUR), Two-Stage Least Squares
(2SLS), Weighted Two-Stage Least Squares (W2SLS), and Three-Stage Least
Squares (3SLS) as suggested, e.g., by Zellner (1962)
<doi:10.2307/2281644>, Zellner and Theil (1962) <doi:10.2307/1911287>, and
Schmidt (1990) <doi:10.1016/0304-4076(90)90127-F>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

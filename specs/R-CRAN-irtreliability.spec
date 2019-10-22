%global packname  irtreliability
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Item Response Theory Reliability

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.0
Requires:         R-core >= 2.11.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-fastGHQuad 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ltm 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-fastGHQuad 

%description
Estimation of reliability coefficients for ability estimates and sum
scores from item response theory models as defined in Cheng, Y., Yuan,
K.-H. and Liu, C. (2012) <doi:10.1177/0013164411407315> and Kim, S. and
Feldt, L. S. (2010) <doi:10.1007/s12564-009-9062-8>. The package supports
the 3-PL and generalized partial credit models and includes estimates of
the standard errors of the reliability coefficient estimators, derived in
Andersson, B. and Xin, T. (2018) <doi:10.1177/0013164417713570>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX

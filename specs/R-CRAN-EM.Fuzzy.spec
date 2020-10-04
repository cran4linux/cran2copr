%global packname  EM.Fuzzy
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          EM Algorithm for Maximum Likelihood Estimation by Non-PreciseInformation

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FuzzyNumbers 
BuildRequires:    R-CRAN-DISTRIB 
Requires:         R-CRAN-FuzzyNumbers 
Requires:         R-CRAN-DISTRIB 

%description
The EM algorithm is a powerful tool for computing maximum likelihood
estimates with incomplete data. This package will help to applying EM
algorithm based on triangular and trapezoidal fuzzy numbers (as two kinds
of incomplete data). A method is proposed for estimating the unknown
parameter in a parametric statistical model when the observations are
triangular or trapezoidal fuzzy numbers. This method is based on
maximizing the observed-data likelihood defined as the conditional
probability of the fuzzy data; for more details and formulas see Denoeux
(2011) <doi:10.1016/j.fss.2011.05.022>.

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

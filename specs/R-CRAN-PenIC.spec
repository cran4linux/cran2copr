%global packname  PenIC
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Semiparametric Regression Analysis of Interval-Censored Datausing Penalized Splines

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-splines 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-splines 
Requires:         R-Matrix 
Requires:         R-MASS 

%description
Currently incorporate the generalized odds-rate model (a type of linear
transformation model) for interval-censored data based on penalized
monotonic B-Spline. More methods under other semiparametric models such as
cure model or additive model will be included in future versions. For more
details see Lu, M., Liu, Y., Li, C. and Sun, J. (2019) <arXiv:1912.11703>.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX

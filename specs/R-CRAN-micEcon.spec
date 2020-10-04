%global packname  micEcon
%global packver   0.6-14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.14
Release:          3%{?dist}%{?buildtag}
Summary:          Microeconomic Analysis and Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plm >= 1.1.0
BuildRequires:    R-CRAN-miscTools >= 0.6.1
Requires:         R-CRAN-plm >= 1.1.0
Requires:         R-CRAN-miscTools >= 0.6.1

%description
Various tools for microeconomic analysis and microeconomic modelling, e.g.
estimating quadratic, Cobb-Douglas and Translog functions, calculating
partial derivatives and elasticities of these functions, and calculating
Hessian matrices, checking curvature and preparing restrictions for
imposing monotonicity of Translog functions.

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
%{rlibdir}/%{packname}/INDEX

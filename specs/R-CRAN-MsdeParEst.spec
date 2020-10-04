%global packname  MsdeParEst
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          3%{?dist}%{?buildtag}
Summary:          Parametric Estimation in Mixed-Effects Stochastic DifferentialEquations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-sde 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-sde 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-mvtnorm 
Requires:         R-methods 
Requires:         R-graphics 

%description
Parametric estimation in stochastic differential equations with random
effects in the drift, or in the diffusion or both. Approximate maximum
likelihood methods are used. M. Delattre, V. Genon-Catalot and A. Samson
(2012) <doi:10.1111/j.1467-9469.2012.00813.x> M. Delattre, V.
Genon-Catalot and A. Samson (2015) <doi:10.1051/ps/2015006> M. Delattre,
V. Genon-Catalot and A. Samson (2016) <doi:10.1016/j.jspi.2015.12.003>.

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
%doc %{rlibdir}/%{packname}/COPYRIGHT.rtf
%{rlibdir}/%{packname}/INDEX

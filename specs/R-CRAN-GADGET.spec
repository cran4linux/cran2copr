%global packname  GADGET
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Gaussian Process Approximations for Designing Experiments

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-DiceOptim 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-DiceOptim 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-pbapply 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 

%description
Computes near-optimal Bayesian experimental designs with Gaussian
processes optimization following the algorithm presented by B. Weaver, et
al. (2016) <doi:10.1214/15-BA945> for either physical or sequential
computer experiments.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX

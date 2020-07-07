%global packname  potts
%global packver   0.5-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.9
Release:          3%{?dist}
Summary:          Markov Chain Monte Carlo for Potts Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Do Markov chain Monte Carlo (MCMC) simulation of Potts models (Potts,
1952, <doi:10.1017/S0305004100027419>), which are the multi-color
generalization of Ising models (so, as as special case, also simulates
Ising models). Use the Swendsen-Wang algorithm (Swendsen and Wang, 1987,
<doi:10.1103/PhysRevLett.58.86>) so MCMC is fast. Do maximum composite
likelihood estimation of parameters (Besag, 1975, <doi:10.2307/2987782>,
Lindsay, 1988, <doi:10.1090/conm/080>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

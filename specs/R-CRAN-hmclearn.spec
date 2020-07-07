%global packname  hmclearn
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          2%{?dist}
Summary:          Fit Statistical Models Using Hamiltonian Monte Carlo

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-parallel 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-bayesplot 
Requires:         R-parallel 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 

%description
Provide users with a framework to learn the intricacies of the Hamiltonian
Monte Carlo algorithm with hands-on experience by tuning and fitting their
own models.  All of the code is written in R.  Theoretical references are
listed below:. Neal, Radford (2011) "Handbook of Markov Chain Monte Carlo"
ISBN: 978-1420079418, Betancourt, Michael (2017) "A Conceptual
Introduction to Hamiltonian Monte Carlo" <arXiv:1701.02434>, Thomas, S.,
Tu, W. (2020) "Hamiltonian Monte Carlo"
<doi:10.1002/9781118445112.stat08243>, Gelman, A., Carlin, J. B., Stern,
H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013) "Bayesian Data
Analysis" ISBN: 978-1439840955, Agresti, Alan (2015) "Foundations of
Linear and Generalized Linear Models ISBN: 978-1118730034, Pinheiro, J.,
Bates, D. (2006) "Mixed-effects Models in S and S-Plus" ISBN:
978-1441903174.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

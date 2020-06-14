%global packname  Sim.PLFN
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Simulation of Piecewise Linear Fuzzy Numbers

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
The definition of fuzzy random variable and the methods of simulation from
fuzzy random variables are two challenging statistical problems in three
recent decades. This package is organized based on a special definition of
fuzzy random variable and simulate fuzzy random variable by Piecewise
Linear Fuzzy Numbers (PLFNs); see Coroianua et al. (2013)
<doi:10.1016/j.fss.2013.02.005> for details about PLFNs. Some important
statistical functions are considered for obtaining the membership function
of main statistics, such as mean, variance, summation, standard deviation
and coefficient of variance. Some of applied advantages of 'Sim.PLFN'
package are: (1) Easily generating / simulation a random sample of PLFN,
(2) drawing the membership functions of the simulated PLFNs or the
membership function of the statistical result, and (3) Considering the
simulated PLFNs for arithmetic operation or importing into some
statistical computation. Finally, it must be mentioned that 'Sim.PLFN'
package works on the basis of 'FuzzyNumbers' package.

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

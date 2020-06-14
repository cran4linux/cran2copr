%global packname  mcunit
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          Unit Tests for MC Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-simctest >= 2.6
BuildRequires:    R-CRAN-testthat >= 2.3
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
Requires:         R-CRAN-simctest >= 2.6
Requires:         R-CRAN-testthat >= 2.3
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-methods 

%description
Unit testing for Monte Carlo methods, particularly Markov Chain Monte
Carlo (MCMC) methods, are implemented as extensions of the 'testthat'
package. The MCMC methods check whether the MCMC chain has the correct
invariant distribution. They do not check other properties of successful
samplers such as whether the chain can reach all points, i.e. whether is
recurrent. The tests require the ability to sample from the prior and to
run steps of the MCMC chain. The methodology is described in Gandy and
Scott (2020) <arXiv:2001.06465>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/amstat.csl
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX

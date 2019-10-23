%global packname  greta
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Simple and Scalable Statistical Modelling in R

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    python2-devel
BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-progress >= 1.2.0
BuildRequires:    R-CRAN-tensorflow >= 1.13.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
Requires:         R-CRAN-progress >= 1.2.0
Requires:         R-CRAN-tensorflow >= 1.13.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-future 
Requires:         R-CRAN-coda 
Requires:         R-methods 

%description
Write statistical models in R and fit them by MCMC and optimisation on
CPUs and GPUs, using Google 'TensorFlow'. greta lets you write your own
model like in BUGS, JAGS and Stan, except that you write models right in
R, it scales well to massive datasets, and it’s easy to extend and build
on. See the website for more information, including tutorials, examples,
package documentation, and the greta forum.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX

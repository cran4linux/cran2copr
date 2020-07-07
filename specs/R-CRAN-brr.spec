%global packname  brr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Bayesian Inference on the Ratio of Two Poisson Rates

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-SuppDists 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-hypergeo 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-stringr 
Requires:         R-methods 

%description
Implementation of the Bayesian inference for the two independent Poisson
samples model, using the semi-conjugate family of prior distributions.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

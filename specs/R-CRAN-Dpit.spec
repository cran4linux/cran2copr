%global packname  Dpit
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Distribution Pitting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fitdistrplus 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-moments 
Requires:         R-utils 
Requires:         R-CRAN-fitdistrplus 

%description
Compares distributions with one another in terms of their fit to each
sample in a dataset that contains multiple samples, as described in Joo,
Aguinis, and Bradley (in press). Users can examine the fit of seven
distributions per sample: pure power law, lognormal, exponential, power
law with an exponential cutoff, normal, Poisson, and Weibull. Automation
features allow the user to compare all distributions for all samples with
a single command line, which creates a separate row containing results for
each sample until the entire dataset has been analyzed.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX

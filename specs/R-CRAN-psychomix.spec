%global packname  psychomix
%global packver   1.1-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.8
Release:          1%{?dist}
Summary:          Psychometric Mixture Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-flexmix >= 2.3.7
BuildRequires:    R-CRAN-Formula >= 1.1.0
BuildRequires:    R-CRAN-psychotools >= 0.4.2
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-modeltools 
Requires:         R-CRAN-flexmix >= 2.3.7
Requires:         R-CRAN-Formula >= 1.1.0
Requires:         R-CRAN-psychotools >= 0.4.2
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-lattice 
Requires:         R-CRAN-modeltools 

%description
Psychometric mixture models based on 'flexmix' infrastructure. At the
moment Rasch mixture models with different parameterizations of the score
distribution (saturated vs. mean/variance specification), Bradley-Terry
mixture models, and MPT mixture models are implemented. These mixture
models can be estimated with or without concomitant variables. See
vignette('raschmix', package = 'psychomix') for details on the Rasch
mixture models.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

%global packname  pollimetry
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Estimate Pollinator Body Size and Co-Varying Ecological Traits

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brms >= 2.4.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-repmis 
Requires:         R-CRAN-brms >= 2.4.0
Requires:         R-stats 
Requires:         R-CRAN-repmis 

%description
Tools to estimate pollinator body size and co-varying traits. This package
contains novel Bayesian predictive models of pollinator body size (for
bees and hoverflies) as well as preexisting predictive models for
pollinator body size (currently implemented for ants, bees, butterflies,
flies, moths and wasps) as well as bee tongue length and foraging
distance, total field nectar loads and wing loading. An additional GitHub
repository <https://github.com/liamkendall/pollimetrydata> provides model
objects to use the bodysize function internally. All models are described
in Kendall et al (2018) <doi:10.1101/397604>.

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

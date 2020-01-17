%global packname  fitODBOD
%global packver   1.4.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1.1
Release:          1%{?dist}
Summary:          Modeling Over Dispersed Binomial Outcome Data Using BMD and ABD

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bbmle 
Requires:         R-CRAN-hypergeo 
Requires:         R-stats 
Requires:         R-CRAN-bbmle 

%description
Contains Probability Mass Functions, Cumulative Mass Functions, Negative
Log Likelihood value, parameter estimation and modeling data using
Binomial Mixture Distributions (BMD) (Manoj et al (2013)
<doi:10.5539/ijsp.v2n2p24>) and Alternate Binomial Distributions (ABD)
(Paul (1985) <doi:10.1080/03610928508828990>), also Journal article to use
the package(<doi:10.21105/joss.01505>).

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
%{rlibdir}/%{packname}/INDEX

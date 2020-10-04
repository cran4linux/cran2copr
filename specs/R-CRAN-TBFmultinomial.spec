%global packname  TBFmultinomial
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          TBF Methodology Extension for Multinomial Outcomes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-nnet 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-VGAM 
Requires:         R-nnet 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plotrix 
Requires:         R-methods 

%description
Extends the test-based Bayes factor (TBF) methodology to multinomial
regression models and discrete time-to-event models with competing risks.
The TBF methodology has been well developed and implemented for the
generalised linear model [Held et al. (2015) <doi:10.1214/14-STS510>] and
for the Cox model [Held et al. (2016) <doi:10.1002/sim.7089>].

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

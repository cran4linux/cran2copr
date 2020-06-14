%global packname  hyper2
%global packver   1.0-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          2%{?dist}
Summary:          The Hyperdirichlet Distribution, Mark 2

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-partitions 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-partitions 

%description
A suite of routines for the hyperdirichlet distribution; supersedes the
'hyperdirichlet' package.

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
%doc %{rlibdir}/%{packname}/basketball.R
%doc %{rlibdir}/%{packname}/collusion_curacao1962.R
%doc %{rlibdir}/%{packname}/collusion_detection.R
%doc %{rlibdir}/%{packname}/collusion_stockholm1962.R
%doc %{rlibdir}/%{packname}/counterstrike_random.R
%doc %{rlibdir}/%{packname}/counterstrike.R
%doc %{rlibdir}/%{packname}/curacao1962_candidates.txt
%doc %{rlibdir}/%{packname}/curacao1962_individual_games.R
%doc %{rlibdir}/%{packname}/curacao1962.txt
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/eurovision.R
%doc %{rlibdir}/%{packname}/F1_allyears.R
%doc %{rlibdir}/%{packname}/formula1_2014.txt
%doc %{rlibdir}/%{packname}/formula1_2015.txt
%doc %{rlibdir}/%{packname}/formula1_2016.txt
%doc %{rlibdir}/%{packname}/formula1_2017.txt
%doc %{rlibdir}/%{packname}/formula1.R
%doc %{rlibdir}/%{packname}/home_advantage.Rmd
%doc %{rlibdir}/%{packname}/karpov_kasparov_anand.R
%doc %{rlibdir}/%{packname}/kka_3draws.R
%doc %{rlibdir}/%{packname}/kka_3whites.R
%doc %{rlibdir}/%{packname}/kka_array.R
%doc %{rlibdir}/%{packname}/laura_confidence_interval.R
%doc %{rlibdir}/%{packname}/masterchef_series6_allrounds.R
%doc %{rlibdir}/%{packname}/rowing_analysis.R
%doc %{rlibdir}/%{packname}/rowing_minimal.txt
%doc %{rlibdir}/%{packname}/rowing.txt
%doc %{rlibdir}/%{packname}/skating_analysis.Rmd
%doc %{rlibdir}/%{packname}/skating.txt
%doc %{rlibdir}/%{packname}/stockholm1962_matches.txt
%doc %{rlibdir}/%{packname}/stockholm1962.txt
%doc %{rlibdir}/%{packname}/tennis.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

%global packname  microsynth
%global packver   2.0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.13
Release:          3%{?dist}%{?buildtag}
Summary:          Synthetic Control Methods with Micro- And Meso-Level Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-LowRankQP 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-parallel 
Requires:         R-boot 
Requires:         R-CRAN-survey 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-LowRankQP 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-pracma 
Requires:         R-parallel 

%description
A generalization of the 'Synth' package that is designed for data at a
more granular level (e.g., micro-level). Provides functions to construct
weights (including propensity score-type weights) and run analyses for
synthetic control methods with micro- and meso-level data; see Robbins,
Saunders, and Kilmer (2017) <doi:10.1080/01621459.2016.1213634>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX

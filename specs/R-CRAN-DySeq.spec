%global packname  DySeq
%global packver   0.22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.22
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Dyadic Sequence Analyses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-TraMineR 
BuildRequires:    R-graphics 
Requires:         R-MASS 
Requires:         R-boot 
Requires:         R-CRAN-TraMineR 
Requires:         R-graphics 

%description
Functions for dyadic binary/dichotomous sequence analyses are implemented
in this contribution. The focus is on estimating actor-partner-interaction
models using various approaches, for instances the approach of Bakeman &
Gottman's (1997) <DOI:10.1017/cbo9780511527685>, generalized multi-level
models, and basic Markov models. Moreover, coefficients of one model can
be translated into those of the other models. Finally, simulation-based
power analyses are provided.

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

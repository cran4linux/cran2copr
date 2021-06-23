%global __brp_check_rpaths %{nil}
%global packname  PST
%global packver   0.94
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.94
Release:          3%{?dist}%{?buildtag}
Summary:          Probabilistic Suffix Trees and Variable Length Markov Chains

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-TraMineR 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
Requires:         R-CRAN-TraMineR 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-methods 
Requires:         R-stats4 

%description
Provides a framework for analysing state sequences with probabilistic
suffix trees (PST), the construction that stores variable length Markov
chains (VLMC). Besides functions for learning and optimizing VLMC models,
the PST library includes many additional tools to analyse sequence data
with these models: visualization tools, functions for sequence prediction
and artificial sequences generation, as well as for context and pattern
mining. The package is specifically adapted to the field of social
sciences by allowing to learn VLMC models from sets of individual
sequences possibly containing missing values, and by accounting for case
weights. The library also allows to compute probabilistic divergence
between two models, and to fit segmented VLMC, where sub-models fitted to
distinct strata of the learning sample are stored in a single PST. This
software results from research work executed within the framework of the
Swiss National Centre of Competence in Research LIVES, which is financed
by the Swiss National Science Foundation. The authors are grateful to the
Swiss National Science Foundation for its financial support.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX

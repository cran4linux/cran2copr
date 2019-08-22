%global packname  breakaway
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}
Summary:          Species Richness Estimation and Modeling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Species richness estimation is an important problem in biodiversity
analysis. This package provides methods for total species richness
estimation (observed plus unobserved) and a method for modelling total
diversity with covariates. breakaway() estimates total (observed plus
unobserved) species richness. Microbial diversity datasets are
characterized by a large number of rare species and a small number of
highly abundant species. The class of models implemented by breakaway() is
flexible enough to model both these features. breakaway_nof1() implements
a similar procedure however does not require a singleton count. betta()
provides a method for modelling total diversity with covariates in a way
that accounts for its estimated nature and thus accounts for unobserved
taxa, and betta_random() permits random effects modelling.

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
%{rlibdir}/%{packname}/INDEX

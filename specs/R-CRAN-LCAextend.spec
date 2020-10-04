%global packname  LCAextend
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Latent Class Analysis (LCA) with Familial Dependence in ExtendedPedigrees

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-kinship2 
Requires:         R-boot 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-kinship2 

%description
Latent Class Analysis of phenotypic measurements in pedigrees and model
selection based on one of two methods: likelihood-based cross-validation
and Bayesian Information Criterion. Computation of individual and triplet
child-parents weights in a pedigree is performed using an upward-downward
algorithm. The model takes into account the familial dependence defined by
the pedigree structure by considering that a class of a child depends on
his parents classes via triplet-transition probabilities of the classes.
The package handles the case where measurements are available on all
subjects and the case where measurements are available only on symptomatic
(i.e. affected) subjects. Distributions for discrete (or ordinal) and
continuous data are currently implemented. The package can deal with
missing data.

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

%global packname  TPD
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Methods for Measuring Functional Diversity Based on TraitProbability Density

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ks >= 1.9.2
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-gridExtra >= 0.9
BuildRequires:    R-CRAN-mvtnorm >= 0.8
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-ks >= 1.9.2
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-gridExtra >= 0.9
Requires:         R-CRAN-mvtnorm >= 0.8
Requires:         R-graphics 
Requires:         R-stats 

%description
Tools to calculate trait probability density functions (TPD) at any scale
(e.g. populations, species, communities). TPD functions are used to
compute several indices of functional diversity, as well as its partition
across scales. These indices constitute a unified framework that
incorporates the underlying probabilistic nature of trait distributions
into uni- or multidimensional functional trait-based studies. See Carmona
et al. (2016) <doi:10.1016/j.tree.2016.02.003> for further information.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

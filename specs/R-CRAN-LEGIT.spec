%global packname  LEGIT
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Latent Environmental & Genetic InTeraction (LEGIT) Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-grDevices 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-formula.tools 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-doSNOW 
Requires:         R-utils 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-Hmisc 
Requires:         R-grDevices 
Requires:         R-boot 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-glmnet 

%description
Constructs genotype x environment interaction (GxE) models where G is a
weighted sum of genetic variants (genetic score) and E is a weighted sum
of environments (environmental score) using the alternating optimization
algorithm by Jolicoeur-Martineau et al. (2017) <arXiv:1703.08111>. This
approach has greatly enhanced predictive power over traditional GxE models
which include only a single genetic variant and a single environmental
exposure. Although this approach was originally made for GxE modelling, it
is flexible and does not require the use of genetic and environmental
variables. It can also handle more than 2 latent variables (rather than
just G and E) and 3-way interactions or more. The LEGIT model produces
highly interpretable results and is very parameter-efficient thus it can
even be used with small sample sizes (n < 250). Tools to determine the
type of interaction (vantage sensitivity, diathesis-stress or differential
susceptibility), with any number of genetic variants or environments, are
available <arXiv:1712.04058>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

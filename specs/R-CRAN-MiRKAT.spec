%global packname  MiRKAT
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Microbiome Regression-Based Kernel Association Test

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-PearsonDS 
BuildRequires:    R-CRAN-GUniFrac 
BuildRequires:    R-MASS 
Requires:         R-survival 
Requires:         R-CRAN-PearsonDS 
Requires:         R-CRAN-GUniFrac 
Requires:         R-MASS 

%description
Test for overall association between microbiome composition data with a
continuous or dichotomous outcome via phylogenetic kernels. The phenotype
can be univariate continuous or binary phenotypes (Zhao et al. (2015)
<doi:10.1016/j.ajhg.2015.04.003>), survival outcomes (Plantinga et al.
(2017) <doi:10.1186/s40168-017-0239-9>), multivariate (Zhan et al. (2017)
<doi:10.1002/gepi.22030>) and structured phenotypes (Zhan et al. (2017)
<doi:10.1111/biom.12684>). For all these effect, the microbiome community
effect was modeled nonparametrically through a kernel function, which can
incorporate the phylogenetic tree information.

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
%{rlibdir}/%{packname}/libs

%global packname  KRMM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Kernel Ridge Mixed Model

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-CRAN-robustbase 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-cvTools 
Requires:         R-CRAN-robustbase 

%description
Solves kernel ridge regression, within the the mixed model framework, for
the linear, polynomial, Gaussian, Laplacian and ANOVA kernels. The model
components (i.e. fixed and random effects) and variance parameters are
estimated using the expectation-maximization (EM) algorithm. All the
estimated components and parameters, e.g. BLUP of dual variables and BLUP
of random predictor effects for the linear kernel (also known as RR-BLUP),
are available. The kernel ridge mixed model (KRMM) is described in Jacquin
L, Cao T-V and Ahmadi N (2016) A Unified and Comprehensible View of
Parametric and Kernel Methods for Genomic Prediction with Application to
Rice. Front. Genet. 7:145. <doi:10.3389/fgene.2016.00145>.

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
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX

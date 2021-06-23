%global __brp_check_rpaths %{nil}
%global packname  IDE
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Integro-Difference Equation Spatio-Temporal Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-FRK 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sparseinv 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-Matrix 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spacetime 
Requires:         R-parallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-FRK 
Requires:         R-CRAN-DEoptim 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-sparseinv 

%description
The Integro-Difference Equation model is a linear, dynamical model used to
model phenomena that evolve in space and in time; see, for example,
Cressie and Wikle (2011, ISBN:978-0-471-69274-4) or Dewar et al. (2009)
<doi:10.1109/TSP.2008.2005091>. At the heart of the model is the kernel,
which dictates how the process evolves from one time point to the next.
Both process and parameter reduction are used to facilitate computation,
and spatially-varying kernels are allowed. Data used to estimate the
parameters are assumed to be readings of the process corrupted by Gaussian
measurement error. Parameters are fitted by maximum likelihood, and
estimation is carried out using an evolution algorithm.

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

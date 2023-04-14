%global __brp_check_rpaths %{nil}
%global packname  GsymPoint
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation of the Generalized Symmetry Point, an OptimalCutpoint in Continuous Diagnostic Tests

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-ROCR 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-ROCR 

%description
Estimation of the cutpoint defined by the Generalized Symmetry point in a
binary classification setting based on a continuous diagnostic test or
marker. Two methods have been implemented to construct confidence
intervals for this optimal cutpoint, one based on the Generalized Pivotal
Quantity and the other based on Empirical Likelihood. Numerical and
graphical outputs for these two methods are easily obtained.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}

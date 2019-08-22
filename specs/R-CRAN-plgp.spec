%global packname  plgp
%global packver   1.1-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          1%{?dist}
Summary:          Particle Learning of Gaussian Processes

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4
Requires:         R-core >= 2.4
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tgp 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tgp 

%description
Sequential Monte Carlo inference for fully Bayesian Gaussian process (GP)
regression and classification models by particle learning (PL).  The
sequential nature of inference and the active learning (AL) hooks provided
facilitate thrifty sequential design (by entropy) and optimization (by
improvement) for classification and regression models, respectively. This
package essentially provides a generic PL interface, and functions
(arguments to the interface) which implement the GP models and AL
heuristics.  Functions for a special, linked, regression/classification GP
model and an integrated expected conditional improvement (IECI) statistic
is provides for optimization in the presence of unknown constraints.
Separable and isotropic Gaussian, and single-index correlation functions
are supported. See the examples section of ?plgp and demo(package="plgp")
for an index of demos

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs

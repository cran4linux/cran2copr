%global packname  lmeNBBayes
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          2%{?dist}
Summary:          Compute the Personalized Activity Index Based on a FlexibleBayesian Negative Binomial Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
The functions in this package implement the safety monitoring procedures
proposed in the paper titled "A flexible mixed effect negative binomial
regression model for detecting unusual increases in MRI lesion counts in
individual multiple sclerosis patients" by Kondo, Y., Zhao, Y. and Petkau,
A.J. The procedure first models longitudinally collected count variables
with a negative binomial mixed-effect regression model. To account for the
correlation among repeated measures from the same patient, the model has
subject-specific random intercept, which is modelled with the infinite
mixture of Beta distributions, very flexible distribution that
theoretically allows any form. The package also has the option of a single
beta distribution for random effects. These mixed-effect models could be
useful beyond the application of the safety monitoring. The inference is
based on MCMC samples and this package contains a Gibbs sampler to sample
from the posterior distribution of the negative binomial mixed-effect
regression model. Based on the fitted model, the personalized activity
index is computed for each patient. Lastly, this package is companion to R
package lmeNB, which contains the functions to compute the Personalized
Activity Index in the frequentist framework.

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
%{rlibdir}/%{packname}/libs

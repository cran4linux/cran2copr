%global __brp_check_rpaths %{nil}
%global packname  lmeNB
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Compute the Personalized Activity Index Based on a NegativeBinomial Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-lmeNBBayes 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-lmeNBBayes 

%description
The functions in this package implement the safety monitoring procedures
proposed in the paper titled "Detection of unusual increases in MRI lesion
counts in individual multiple sclerosis patients" by Zhao, Y., Li, D.K.B.,
Petkau, A.J., Riddehough, A., Traboulsee, A., published in Journal of the
American Statistical Association in 2013. The procedure first models
longitudinally collected count variables with a negative binomial
mixed-effect regression model. To account for the correlation among
repeated measures from the same patient, the model has subject-specific
random intercept, which can be modelled with a gamma or log-normal
distributions. One can also choose the semi-parametric option which does
not assume any distribution for the random effect. These mixed-effect
models could be useful beyond the application of the safety monitoring.
The maximum likelihood methods are used to estimate the unknown fixed
effect parameters of the model. Based on the fitted model, the
personalized activity index is computed for each patient. Lastly, this
package is companion to R package lmeNBBayes, which contains the functions
to compute the Personalized Activity Index in Bayesian framework.

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

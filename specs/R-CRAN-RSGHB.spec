%global __brp_check_rpaths %{nil}
%global packname  RSGHB
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Hierarchical Bayesian Estimation: A Flexible Approach

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-CRAN-MCMCpack 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions for estimating models using a Hierarchical Bayesian (HB)
framework. The flexibility comes in allowing the user to specify the
likelihood function directly instead of assuming predetermined model
structures. Types of models that can be estimated with this code include
the family of discrete choice models (Multinomial Logit, Mixed Logit,
Nested Logit, Error Components Logit and Latent Class) as well ordered
response models like ordered probit and ordered logit. In addition, the
package allows for flexibility in specifying parameters as either fixed
(non-varying across individuals) or random with continuous distributions.
Parameter distributions supported include normal, positive/negative
log-normal, positive/negative censored normal, and the Johnson SB
distribution. Kenneth Train's Matlab and Gauss code for doing Hierarchical
Bayesian estimation has served as the basis for a few of the functions
included in this package. These Matlab/Gauss functions have been rewritten
to be optimized within R. Considerable code has been added to increase the
flexibility and usability of the code base. Train's original Gauss and
Matlab code can be found here:
<http://elsa.berkeley.edu/Software/abstracts/train1006mxlhb.html> See
Train's chapter on HB in Discrete Choice with Simulation here:
<http://elsa.berkeley.edu/books/choice2.html>; and his paper on using HB
with non-normal distributions here:
<http://eml.berkeley.edu//~train/trainsonnier.pdf>. The authors would also
like to thank the invaluable contributions of Stephane Hess and the Choice
Modelling Centre: <https://cmc.leeds.ac.uk/>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}

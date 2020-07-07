%global packname  presmTP
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Methods for Transition Probabilities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survPresmooth 
BuildRequires:    R-mgcv 
Requires:         R-CRAN-survPresmooth 
Requires:         R-mgcv 

%description
Provides a function for estimating the transition probabilities in an
illness-death model. The transition probabilities can be estimated from
the unsmoothed landmark estimators developed by de Una-Alvarez and
Meira-Machado (2015) <doi:10.1111/biom.12288>. Presmoothed estimates can
also be obtained through the use of a parametric family of binary
regression curves, such as logit, probit or cauchit. The additive logistic
regression model and nonparametric regression are also alternatives which
have been implemented. The idea behind the presmoothed landmark estimators
is to use the presmoothing techniques developed by Cao et al. (2005)
<doi:10.1007/s00180-007-0076-6> in the landmark estimation of the
transition probabilities.

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
%{rlibdir}/%{packname}/INDEX

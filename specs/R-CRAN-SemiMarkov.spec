%global __brp_check_rpaths %{nil}
%global packname  SemiMarkov
%global packver   1.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.6
Release:          3%{?dist}%{?buildtag}
Summary:          Multi-States Semi-Markov Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rsolnp 
Requires:         R-CRAN-numDeriv 
Requires:         R-MASS 
Requires:         R-CRAN-Rsolnp 

%description
Functions for fitting multi-state semi-Markov models to longitudinal data.
A parametric maximum likelihood estimation method adapted to deal with
Exponential, Weibull and Exponentiated Weibull distributions is
considered. Right-censoring can be taken into account and both constant
and time-varying covariates can be included using a Cox proportional
model. Reference: A. Krol and P. Saint-Pierre (2015)
<doi:10.18637/jss.v066.i06>.

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

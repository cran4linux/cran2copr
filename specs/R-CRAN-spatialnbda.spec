%global packname  spatialnbda
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Performs spatial NBDA in a Bayesian context

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-SocialNetworks >= 1.1
BuildRequires:    R-CRAN-mvtnorm >= 0.9
Requires:         R-CRAN-SocialNetworks >= 1.1
Requires:         R-CRAN-mvtnorm >= 0.9

%description
Network based diffusion analysis (NBDA) allows inference on the asocial
and social transmission of information.  This may involve the social
transmission of a particular behaviour such as tool use, for example. For
the NBDA, the key parameters estimated are the social effect and baseline
rate parameters.  The baseline rate parameter gives the rate at which the
behaviour is first performed (or acquired) asocially amongst the
individuals in a given population. The social effect parameter quantifies
the effect of the social associations amongst the individuals on the rate
at which each individual first performs or displays the behaviour.
Spatial NBDA involves incorporating spatial information in the analysis.
This is done by incorporating social networks derived from spatial point
patterns (of the home bases of the individuals under study).  In addition,
a spatial covariate such as vegetation cover, or slope may be included in
the modelling process.

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

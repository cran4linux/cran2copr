%global packname  gmnl
%global packver   1.1-3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3.1
Release:          1%{?dist}
Summary:          Multinomial Logit Models with Random Parameters

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-mlogit 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-mlogit 
Requires:         R-CRAN-truncnorm 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
An implementation of maximum simulated likelihood method for the
estimation of multinomial logit models with random coefficients.
Specifically, it allows estimating models with continuous heterogeneity
such as the mixed multinomial logit and the generalized multinomial logit.
It also allows estimating models with discrete heterogeneity such as the
latent class and the mixed-mixed multinomial logit model.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX

%global packname  MarginalMediation
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          3%{?dist}%{?buildtag}
Summary:          Marginal Mediation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-furniture 
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-boot 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-furniture 
Requires:         R-CRAN-betareg 
Requires:         R-CRAN-stringr 

%description
Provides the ability to perform "Marginal Mediation"--mediation wherein
the indirect and direct effects are in terms of the average marginal
effects (Bartus, 2005,
<https://EconPapers.repec.org/RePEc:tsj:stataj:v:5:y:2005:i:3:p:309-329>).
The style of the average marginal effects stems from Thomas Leeper's work
on the "margins" package. This framework allows the use of categorical
mediators and outcomes with little change in interpretation from the
continuous mediators/outcomes. See <doi:10.13140/RG.2.2.18465.92001> for
more details on the method.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

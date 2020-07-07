%global packname  powerlmm
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}
Summary:          Power Analysis for Longitudinal Multilevel Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.1
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
Requires:         R-CRAN-lme4 >= 1.1
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-scales 
Requires:         R-utils 

%description
Calculate power for the 'time x treatment' effect in two- and three-level
multilevel longitudinal studies with missing data. Both the third-level
factor (e.g. therapists, schools, or physicians), and the second-level
factor (e.g. subjects), can be assigned random slopes. Studies with
partially nested designs, unequal cluster sizes, unequal allocation to
treatment arms, and different dropout patterns per treatment are
supported. For all designs power can be calculated both analytically and
via simulations. The analytical calculations extends the method described
in Galbraith et al. (2002) <doi:10.1016/S0197-2456(02)00205-2>, to
three-level models. Additionally, the simulation tools provides flexible
ways to investigate bias, Type I errors and the consequences of model
misspecification.

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
%doc %{rlibdir}/%{packname}/shiny_powerlmm
%{rlibdir}/%{packname}/INDEX

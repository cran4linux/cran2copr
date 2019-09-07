%global packname  squid
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Statistical Quantification of Individual Differences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.51.1
BuildRequires:    R-grid >= 3.5.3
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-shiny >= 1.3.2
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-arm >= 1.10.1
BuildRequires:    R-CRAN-lme4 >= 1.1.21
BuildRequires:    R-stats 
Requires:         R-MASS >= 7.3.51.1
Requires:         R-grid >= 3.5.3
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-shiny >= 1.3.2
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-arm >= 1.10.1
Requires:         R-CRAN-lme4 >= 1.1.21
Requires:         R-stats 

%description
A simulation-based tool made to help researchers to become familiar with
multilevel variations, and to build up sampling designs for their study.
This tool has two main objectives: First, it provides an educational tool
useful for students, teachers and researchers who want to learn to use
mixed-effects models. Users can experience how the mixed-effects model
framework can be used to understand distinct biological phenomena by
interactively exploring simulated multilevel data. Second, it offers
research opportunities to those who are already familiar with
mixed-effects models, as it enables the generation of data sets that users
may download and use for a range of simulation-based statistical analyses
such as power and sensitivity analysis of multilevel and multivariate data
[Allegue, H., Araya-Ajoy, Y.G., Dingemanse, N.J., Dochtermann N.A.,
Garamszegi, L.Z., Nakagawa, S., Reale, D., Schielzeth, H. and Westneat,
D.F. (2016) <doi: 10.1111/2041-210X.12659>].

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/shiny-squid
%{rlibdir}/%{packname}/INDEX

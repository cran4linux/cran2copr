%global packname  horserule
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Flexible Non-Linear Regression with the HorseRule Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-inTrees 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvnfast 
Requires:         R-MASS 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-inTrees 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 

%description
Implementation of the HorseRule model a flexible tree based Bayesian
regression method for linear and nonlinear regression described in Nalenz
& Villani (2017) <arXiv:1702.05008>.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%doc %{rlibdir}/%{packname}/texput.log
%{rlibdir}/%{packname}/INDEX

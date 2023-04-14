%global __brp_check_rpaths %{nil}
%global packname  plotSEMM
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          3%{?dist}%{?buildtag}
Summary:          Graphing Nonlinear Relations Among Latent Variables fromStructural Equation Mixture Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MplusAutomation 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-shiny 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-MplusAutomation 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-plotrix 

%description
Contains a graphical user interface to generate the diagnostic plots
proposed by Bauer (2005; <doi:10.1207/s15328007sem1204_1>), Pek & Chalmers
(2015; <doi:10.1080/10705511.2014.937790>), and Pek, Chalmers, R. Kok, &
Losardo (2015; <doi:10.3102/1076998615589129>) to investigate nonlinear
bivariate relationships in latent regression models using structural
equation mixture models (SEMMs).

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

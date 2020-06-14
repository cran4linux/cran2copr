%global packname  caRamel
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Automatic Calibration by Evolutionary Multi Objective Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-parallel 
Requires:         R-CRAN-geometry 
Requires:         R-parallel 

%description
Multi-objective optimizer initially developed for the calibration of
hydrological models. The algorithm is a hybrid of the MEAS algorithm
(Efstratiadis and Koutsoyiannis (2005) <doi:10.13140/RG.2.2.32963.81446>)
by using the directional search method based on the simplexes of the
objective space and the epsilon-NGSA-II algorithm with the method of
classification of the parameter vectors archiving management by
epsilon-dominance (Reed and Devireddy <doi:10.1142/9789812567796_0004>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX

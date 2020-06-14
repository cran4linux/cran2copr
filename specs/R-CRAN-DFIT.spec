%global packname  DFIT
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          Differential Functioning of Items and Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-simex 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-simex 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 

%description
A set of functions to perform Raju, van der Linden and Fleer's (1995,
doi:10.1177/014662169501900405) Differential Functioning of Items and
Tests (DFIT) analyses. It includes functions to use the Monte Carlo Item
Parameter Replication approach (Oshima, Raju, & Nanda, 2006,
doi:10.1111/j. 1745-3984.2006.00001.x) for obtaining the associated
statistical significance tests cut-off points. They may also be used for a
priori and post-hoc power calculations (Cervantes, 2017,
doi:10.18637/jss.v076.i05).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
